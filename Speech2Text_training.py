import keras
from keras.utils import np_utils
from keras.layers import Bidirectional, BatchNormalization, GRU, Dense, Dropout, Flatten, Conv1D, Input, MaxPooling1D
from keras.models import Model
from keras.callbacks import EarlyStopping, ModelCheckpoint
from tensorflow.keras import backend as K
import librosa
import scipy
from scipy.io import wavfile
import sklearn
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import sounddevice as sd
import tensorflow as tf
import numpy as np
import os
import glob


train_audio_path = 'Dataset/train/audio'
all_wave = []
all_label = []

trainLabels = np.array(os.listdir(train_audio_path))

for label in trainLabels:
    print(label)
    waves = [f for f in os.listdir(train_audio_path + '/' + label) if 
             f.endswith('.wav')]
    for wav in waves:
        samples, sample_rate = librosa.load(train_audio_path + '/' +
                                            label + '/' + wav, sr = 16000)
        samples = librosa.resample(samples, sample_rate, 8000)
        if (len(samples) == 8000):
            all_wave.append(samples)
            all_label.append(label)

label_encoder = LabelEncoder()
y = label_encoder.fit_transform(all_label)
classes = list(label_encoder.classes_)
y = np_utils.to_categorical(y, num_classes=len(trainLabels))

all_wave = np.array(all_wave).reshape(-1, 8000, 1)

x_train, x_valid, y_train, y_valid = train_test_split(np.array(all_wave),np.array(y),
                                                      stratify=y,test_size = 0.2, random_state = 777, shuffle=True)

#Build the model

model = keras.Sequential()

model.add(BatchNormalization(axis=-1, momentum=0.99, epsilon=1e-3, center=True, scale=True))

model.add(Conv1D(8,13, padding='valid', activation='relu', strides=1))
model.add(MaxPooling1D(3))
model.add(Dropout(0.3))

model.add(Conv1D(16, 11, padding='valid', activation='relu', strides=1))
model.add(MaxPooling1D(3))
model.add(Dropout(0.3))

model.add(Conv1D(32, 9, padding='valid', activation='relu', strides=1))
model.add(MaxPooling1D(3))
model.add(Dropout(0.3))

model.add(BatchNormalization(axis=-1, momentum=0.99, epsilon=1e-3, center=True, scale=True))

model.add(Bidirectional(GRU(128, return_sequences=True), merge_mode='sum'))
model.add(Bidirectional(GRU(128, return_sequences=True), merge_mode='sum'))
model.add(Bidirectional(GRU(128, return_sequences=False), merge_mode='sum'))

model.add(BatchNormalization(axis=-1, momentum=0.99, epsilon=1e-3, center=True, scale=True))

model.add(Dense(256, activation='relu'))
model.add(Dense(len(trainLabels), activation="softmax"))

model.compile(loss='categorical_crossentropy', optimizer='nadam', metrics=['accuracy'])

early_stop = EarlyStopping(monitor='val_loss', mode='min', verbose=1, patience=10, min_delta=0.0001)
checkpoint = ModelCheckpoint(filepath='speechRecogModel.h5', monitor='val_accuracy', verbose=1, save_best_only=True, mode='max')


model.fit(
    x=x_train,
    y=y_train,
    epochs=100,
    batch_size=32,
    callbacks=[early_stop, checkpoint],
    validation_data=(x_valid, y_valid),
    )

model.summary()




import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import string
from gtts import gTTS
from docx import Document

def get_data(doc_filename) {
    #assuming the gui processes the file and puts it in the same directory as the code
    filename = doc_filename
    file = open(filename, 'rt')
    docs = file.read()
    file.close()
    return docs
    }

def tts(docs) {
    tts = gTTS(docs, lang='en')
    return tts
    }

def extract_data(docs) {
    tokens = word_tokenize(docs)
    tokens = [w.lower() for w in tokens]
    table = str.maketrans('', '', string.punctuation)
    stripped = [w.translate(table) for w in tokens]
    stop_words = seet(stropwords.words('english'))
    words = [w for w in words if not w in stop_words]
    #stem words for accurate graphing
    porter = PorterStemmer
    stemmed = [porter.stem(word) for word in tokens]
    
    }

def vis_data(dataextr) {
    ##build a graph using dataextr
    ##turn it to an img
    #return img to console
    }

#make an ai for??? uh


def runprog(document){
    dataout = get_data(document)
    speech = tts(dataout)
    dataextr = extract_data(document)
    img = vis_data(dataextr)
    return speech, img
    }

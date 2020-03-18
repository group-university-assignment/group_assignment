import nltk
import gTTS
from docx import Document

def get_data(docs) {
    ##get document passed to this function (docx or txt)
    #clean doc
    #turn to string
    #return string dataout
    }

def tts(dataout) {
    #turn string to speech
    ##return speech.mp3
    }

def extract_data(docs) {
    ##get document passed to this function
    ##make a wordlist of fufw
    ##extract fuw from doc and remove fufw
    ##return dataextr
    }

def vis_data(dataextr) {
    ##build a graph using dataextr
    ##turn it to an img
    #return img to console
    }

def runprog(document){
    dataout = get_data(document)
    speech = tts(dataout)
    dataextr = extract_data(document)
    img = vis_data(dataextr)
    return speech, img
    }

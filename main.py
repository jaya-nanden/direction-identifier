import speech_recognition as sr
import pyttsx3

import re

from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.tokenize.treebank import TreebankWordDetokenizer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from textblob import TextBlob


from intent_response import *

print("------------------- Intialiazing Your Assistant -------------------")


def voice_output(msg):
    print("Assistant: " + msg)
    engine = pyttsx3.init()
    engine.setProperty('rate', 100)
    engine.setProperty('volume', 0.7)
    engine.say(str(msg))
    engine.runAndWait()


def speech_input(listen):
    r = sr.Recognizer()
    with sr.Microphone() as src:
        print("------------------- Listening -------------------")
        print("Speak: " , end=" ")
        input_audio = r.record(src, duration=listen)
        converted_text = ''
        try:
            converted_text = r.recognize_google(input_audio)
            # print('Speaker : {}'.format(converted_text))
            print(converted_text)
        except:
            print('Going sleep for 3 secs')

    return converted_text

def match_intent(msg, patterns):
    msg = msg.lower()
    matched_intent = None
    for intent, pattern in patterns.items():
        if re.search(pattern, msg):
            matched_intent = intent

    return matched_intent


def respond(msg):
    response_intent = match_intent(msg, patterns)
    keys = 'default'
    if response_intent == 'stop':
        keys = 'stop'
    elif response_intent in responses:
        keys = response_intent

    return keys


def process_msg(msg):

    gfg = TextBlob(msg)
    gfg = str(gfg.correct())
    a = word_tokenize(gfg)
    lem = WordNetLemmatizer()
    b = []
    for w in a:
        b.append(lem.lemmatize(w))
    c = TreebankWordDetokenizer().detokenize(b)

    return c

voice_output("Hi, I am your voice assistant")

flag = 1
while(flag):
    user_input = speech_input(listen=5)
    words = process_msg(user_input)
    key = respond(words)
    if(key != "default"):
        voice_output(responses[key][0])
        if(key == "stop"):
            flag = 0


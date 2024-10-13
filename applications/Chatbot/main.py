from applications.Chatbot.responses.responses2 import responses1
from applications.Chatbot.responses.responses import responses2

from applications.Chatbot.commands.mathmodel import MathModel

import random
import time
import datetime

weightedWords = {}
sentenceWeights = {}

lastResponse = False

responses = responses1 + responses2

class App:
    def __init__(self, username):
        self.name = "Chatbot"
        self.username = username

        print(f"          loading {self.name}")

    def run(self):
        print(f"starting {self.name}")
        time.sleep(1)
        running = True
        while running:
            input_ = input("(n to close) you: ")
            if input_ == "n":
                running = False
            else:
                print(chatbot(input_)[0])
        time.sleep(1)

def weightExists(input_):
    try:
        a = weightedWords[input_]
        return True
    except:
        return False

def weightWords():
    for question in responses:
        sentenceWeights[question[0]] = 1
        for word_ in question[0].split(" "):
            word = word_.replace("?", "").replace(".", "").replace("!", "").replace(",", "")
            if not weightExists(word):
                weightedWords[word] = 1
            else:
                weightedWords[word] += 1

def responseExists(input_):
    try:
        a = responses[input_]
        return True
    except:
        return False

def chatbot(text):
    global sentenceWeights
    global lastResponse

    weights = getWeights(text)
    _word_ = responses[weights.index(max(weights))][1][random.randint(0, len(responses[weights.index(max(weights))][1]) - 1)]

    if _word_ == "lnmathmodel" and not "explain" in text:
        return [MathModel(text, False), False]
    if _word_ == "lnmathmodelexplain" or (_word_ == "lnmathmodel" and "explain" in text):
        return [MathModel(text, True), False]

    if "```" in text and False:
        return EmulatePython(text)
    elif _word_ == "_dateDay_":
        _word_ = ["monday", "theusday", "wednessday", "thursday", "friday", "saturday", "sunday"][datetime.datetime.today().weekday()]
        lastResponse = responses[weights.index(max(weights))][0]
        return [_word_, False]
    elif _word_ == "_dateDay2_":
        dayIndex = datetime.datetime.today().weekday() + 1
        if dayIndex == 7:
            dayIndex = 0
        _word_ = ["monday", "theusday", "wednessday", "thursday", "friday", "saturday", "sunday"][dayIndex]
        lastResponse = responses[weights.index(max(weights))][0]
        return [_word_, False]
    elif _word_ == "_dateDay3_":
        dayIndex = datetime.datetime.today().weekday() - 1
        if dayIndex == -1:
            dayIndex = 6
        _word_ = ["monday", "theusday", "wednessday", "thursday", "friday", "saturday", "sunday"][dayIndex]
        lastResponse = responses[weights.index(max(weights))][0]
        return [_word_, False]
    
    if _word_[0] == "_":
        lastResponse = responses[weights.index(max(weights))][0]
        return ["This command is dissabled :c", False]
    else:
        lastResponse = responses[weights.index(max(weights))][0]
        return [_word_, False]

def getWeights(text):
    weights_ = []
    words = text.lower().replace("?", "").replace(".", "").replace("!", "").replace(",", "").split(" ")

    for word in responses:
        word__ = word[0].replace("?", "").replace(".", "").replace("!", "").replace(",", "")

        if word__ == "":
            weights_.append(0)
            continue
        weight = 0
        for word_ in words:
            if word_.lower() in word__.lower().split(" "):
                if weightExists(word_.lower()):
                    weight += (5 / (len(word__.split(" ")) + 1)) * word__.lower().split(" ").count(word_.lower()) * sentenceWeights[word[0]] * (1 / weightedWords[word_.lower()])
                else:
                    weight += (5 / ((len(word__.split(" ")) + 1) / 5)) * word__.lower().split(" ").count(word_.lower())
            if word_.lower() in word__.lower():
                if weightExists(word_.lower()):
                    weight += (2.5 / (len(word__.split(" ")) + 1)) * word__.lower().split(" ").count(word_.lower()) * sentenceWeights[word[0]] * (1 / weightedWords[word_.lower()])
                else:
                    weight += (2.5 / (len(word__.split(" ")) + 1))
            if word__.lower() in word_.lower():
                if weightExists(word_.lower()):
                    weight += (1 / (len(word__.split(" ")) + 1)) * word__.lower().split(" ").count(word_.lower()) * sentenceWeights[word[0]] * (1 / weightedWords[word_.lower()])
                else:
                    weight += (1 / (len(word__.split(" ")) + 1)) * word__.lower().split(" ").count(word_.lower())
        weights_.append(weight)
    
    return weights_
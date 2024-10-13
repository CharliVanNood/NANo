import time
import random
import datetime

from applications.diary.commands import commands

# we have to ask the user to submit a date, but that can be in multiple ways so a chatbot is used

weightedWords = {}
sentenceWeights = {}

class App:
    def __init__(self, username):
        self.name = "Diary"
        self.username = username

        print(f"          loading {self.name}")

    def run(self):
        print(f"starting {self.name}")
        self.weightWords()
        time.sleep(1)
        running = True
        while running:
            input_ = input("when did this action happen? (submit 2 words or more for verification, n to cancel): ")
            if input_ == "n":
                running = False
            elif len(input_.split(" ")) >= 2:
                time_ = self.query(input_)
                
                text_ = input("what happened?: ")
                timeSec = 0

                if time_ == "_noteToday_":
                    timeSec = time.time()
                elif time_ == "_noteYesterday_":
                    timeSec = time.time() - 60 * 60 * 24
                elif time_ == "_noteTomorrow_":
                    timeSec = time.time() + 60 * 60 * 24
                elif time_ == "_noteInNumber_":
                    number_ = 0
                    for word in input_.split(" "):
                        if word.isnumeric():
                            number_ = float(word)
                            print(f"in {number_} days {text_}")
                    timeSec = time.time() + 60 * 60 * 24 * number_
                elif time_ == "_noteInNumberAgo_":
                    number_ = 0
                    for word in input_.split(" "):
                        if word.isnumeric():
                            number_ = float(word)
                            print(f"{number_} days ago {text_}")
                    timeSec = time.time() - 60 * 60 * 24 * number_


    def query(self, input_):
        weights = self.getWeights(input_)
        return commands[weights.index(max(weights))][1][random.randint(0, len(commands[weights.index(max(weights))][1]) - 1)]

    def weightWords(self):
        print("weighting words")
        for question in commands:
            sentenceWeights[question[0]] = 1
            for word_ in question[0].split(" "):
                word = word_.replace("?", "").replace(".", "").replace("!", "").replace(",", "")
                if not self.weightExists(word):
                    weightedWords[word] = 1
                else:
                    weightedWords[word] += 1

    def weightExists(self, input_):
        try:
            a = weightedWords[input_]
            return True
        except:
            return False
    
    def getWeights(self, text):
        weights_ = []
        words = text.lower().replace("?", "").replace(".", "").replace("!", "").replace(",", "").split(" ")

        for word in commands:
            word__ = word[0].replace("?", "").replace(".", "").replace("!", "").replace(",", "")

            if word__ == "":
                weights_.append(0)
                continue
            weight = 0
            for word_ in words:
                if word_.lower() == "nyo" or word_.lower() == "bot": continue
                if word_.lower() in word__.lower().split(" "):
                    if self.weightExists(word_.lower()):
                        weight += (5 / (len(word__.split(" ")) + 1)) * word__.lower().split(" ").count(word_.lower()) * sentenceWeights[word[0]] * (1 / weightedWords[word_.lower()])
                    else:
                        weight += (5 / ((len(word__.split(" ")) + 1) / 5)) * word__.lower().split(" ").count(word_.lower())
                if word_.lower() in word__.lower():
                    if self.weightExists(word_.lower()):
                        weight += (2.5 / (len(word__.split(" ")) + 1)) * word__.lower().split(" ").count(word_.lower()) * sentenceWeights[word[0]] * (1 / weightedWords[word_.lower()])
                    else:
                        weight += (2.5 / (len(word__.split(" ")) + 1))
                if word__.lower() in word_.lower():
                    if self.weightExists(word_.lower()):
                        weight += (1 / (len(word__.split(" ")) + 1)) * word__.lower().split(" ").count(word_.lower()) * sentenceWeights[word[0]] * (1 / weightedWords[word_.lower()])
                    else:
                        weight += (1 / (len(word__.split(" ")) + 1)) * word__.lower().split(" ").count(word_.lower())
            weights_.append(weight)
    
        return weights_
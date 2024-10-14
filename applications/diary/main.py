import time
import random
import datetime
import math

from applications.diary.commands import commands

# we have to ask the user to submit a date, but that can be in multiple ways so a chatbot is used

weightedWords = {}
sentenceWeights = {}

class App:
    def __init__(self, username):
        self.name = "diary"
        self.username = username

        print(f"          loading {self.name}")

    def run(self):
        print(f"starting {self.name}")
        self.weightWords()
        time.sleep(1)
        action = ""
        while action == "":
            action_ = input("read (r), add (a), edit (e), exit (n): ")
            if action_ == "r" or action_ == "a" or action_ == "e" or action_ == "n":
                action = action_

        if action == "a":
            running = True
            while running:
                input_ = input("when did this action happen? (n to cancel): ")
                if input_ == "n":
                    running = False
                else:
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

                    with open(f"applications/{self.name}/diary.csv", "a") as f:
                        f.write(f"\n{timeSec}, {text_}")
        elif action == "e":
            input_ = input("what day? (n to cancel): ")
            if input_ == "n":
                running = False
            else:
                time_ = self.query(input_)
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
                    timeSec = time.time() + 60 * 60 * 24 * number_
                elif time_ == "_noteInNumberAgo_":
                    number_ = 0
                    for word in input_.split(" "):
                        if word.isnumeric():
                            number_ = float(word)
                    timeSec = time.time() - 60 * 60 * 24 * number_

            closest = [10000000, 0, 0]
            data = []

            with open(f"applications/{self.name}/diary.csv", "r") as f:
                data_ = f.readlines()
                lines = []
                lineIndex = 0
                for line in data_:
                    if line == "": continue
                    if lineIndex > 0:
                        lineData = line.split(",")
                        data.append([float(lineData[0]), lineData[1]])
                    lineIndex += 1

            i = 0
            for line in data:
                if abs(line[0] - timeSec) < closest[0]:
                    closest[0] = abs(line[0] - timeSec)
                    closest[1] = i
                    closest[2] = abs(line[0] - time.time())
                i += 1
            
            amountOfDays = math.floor(closest[2] / (60 * 60 * 24))
            print(f"found a log {amountOfDays} days ago")
            print(data[closest[1]][1])
            print("")
            edit = input("edit (y / n): ")
            if edit == "y":
                text_ = input("new text: ")
                data[closest[1]][1] = " " + text_

            fileOut = "time,data\n"
            for line in data:
                data_ = line[1].replace('\n', '')[1:]
                fileOut += f"{line[0]}, {data_}\n"
            
            with open(f"applications/{self.name}/diary.csv", "w") as f:
                f.write(fileOut)

        elif action == "r":
            input_ = input("what day? (n to cancel): ")
            if input_ == "n":
                running = False
            else:
                time_ = self.query(input_)
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
                    timeSec = time.time() + 60 * 60 * 24 * number_
                elif time_ == "_noteInNumberAgo_":
                    number_ = 0
                    for word in input_.split(" "):
                        if word.isnumeric():
                            number_ = float(word)
                    timeSec = time.time() - 60 * 60 * 24 * number_

            closest = [10000000, 0, 0]
            data = []

            with open(f"applications/{self.name}/diary.csv", "r") as f:
                data_ = f.readlines()
                lines = []
                lineIndex = 0
                for line in data_:
                    if line == "": continue
                    if lineIndex > 0:
                        lineData = line.split(",")
                        data.append([float(lineData[0]), lineData[1]])
                    lineIndex += 1

            i = 0
            for line in data:
                if abs(line[0] - timeSec) < closest[0]:
                    closest[0] = abs(line[0] - timeSec)
                    closest[1] = i
                    closest[2] = abs(line[0] - time.time())
                i += 1
            
            amountOfDays = math.floor(closest[2] / (60 * 60 * 24))
            print(f"found a log {amountOfDays} days ago")
            print(data[closest[1]][1])
            print("")
            input("press enter to return")
        
        time.sleep(1)


    def query(self, input_):
        weights = self.getWeights(input_)
        return commands[weights.index(max(weights))][1][random.randint(0, len(commands[weights.index(max(weights))][1]) - 1)]

    def weightWords(self):
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
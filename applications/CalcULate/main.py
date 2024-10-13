import random
import time

class App:
    def __init__(self, username):
        self.name = "CalcULate"
        self.username = username

        print(f"          loading {self.name}")

    def run(self):
        print(f"starting {self.name}")
        time.sleep(1)
        print("")
        text = input("(n to close): ")
        if text == "n":
            time.sleep(1)
            return
        else:
            if len(text.split(" ")) < 2:
                self.run()
            else:
                print(self.MathModel(text, False))
                self.run()


    def MathModel(self, text, explain):
        explanation = ""
        step = 1
        equasion = []

        text_ = text.replace("*", " * ")
        text_ = text_.replace("/", " / ")
        text_ = text_.replace("-", " - ")
        text_ = text_.replace("+", " + ")
        text_ = text_.replace("plus", "+")
        text_ = text_.replace("minus", "-")
        text_ = text_.replace("times", "*")
        text_ = text_.replace("divided by", "/")
        keys = text_.split(" ")

        for key in keys:
            if key.replace(".", "").replace(",", "").isnumeric():
                equasion.append(key)
            elif key == "+" or key == "-" or key == "/" or key == "*":
                equasion.append(key)

        if explain:
            equasion_ = ""
            for key in equasion:
                equasion_ += key + " "
            explanation += "First we take the equasion " + equasion_
            explanation = explanation[:-1] + "\n"
            print(explanation)

        key_ = 0
        while key_ < len(equasion):
            key = equasion[key_]
            if key == "*":
                if explain:
                    if step == 1:
                        explanation += f"Then we'll multiply the number {float(equasion[key_ - 1])} by {float(equasion[key_ + 1])} which results in {float(equasion[key_ - 1]) * float(equasion[key_ + 1])}\n"
                    else:
                        explanation += f"After that we'll multiply the number {float(equasion[key_ - 1])} by {float(equasion[key_ + 1])} which will result in {float(equasion[key_ - 1]) * float(equasion[key_ + 1])}\n"
                    step += 1
                    print(explanation)
                equasion[key_ - 1] = float(equasion[key_ - 1]) * float(equasion[key_ + 1])
                equasion.pop(key_)
                equasion.pop(key_)
                key_ -= 2
            if key == "/":
                if explain:
                    if step == 1:
                        explanation += f"Then we'll devide the number {float(equasion[key_ - 1])} by {float(equasion[key_ + 1])} which results in {round(float(equasion[key_ - 1]) / float(equasion[key_ + 1]), 2)}\n"
                    else:
                        explanation += f"After that we'll devide the number {float(equasion[key_ - 1])} by {float(equasion[key_ + 1])} which will result in {round(float(equasion[key_ - 1]) / float(equasion[key_ + 1]), 2)}\n"
                    step += 1
                    print(explanation)
                equasion[key_ - 1] = round(float(equasion[key_ - 1]) / float(equasion[key_ + 1]), 2)
                equasion.pop(key_)
                equasion.pop(key_)
                key_ -= 2
            key_ += 1

        key_ = 0
        while key_ < len(equasion):
            key = equasion[key_]
            if key == "+":
                if explain:
                    if step == 1:
                        explanation += f"Then we'll add the numbers {float(equasion[key_ - 1])} and {float(equasion[key_ + 1])} together which results in {float(equasion[key_ - 1]) + float(equasion[key_ + 1])}\n"
                    else:
                        if random.randint(0, 1) == 0:
                            explanation += f"After that we'll add the numbers {float(equasion[key_ - 1])} and {float(equasion[key_ + 1])} which results in {float(equasion[key_ - 1]) + float(equasion[key_ + 1])}\n"
                        else:
                            explanation += f"And after that we'll add the numbers {float(equasion[key_ - 1])} and {float(equasion[key_ + 1])} which will results in {float(equasion[key_ - 1]) + float(equasion[key_ + 1])}\n"
                    step += 1
                    print(explanation)
                equasion[key_ - 1] = float(equasion[key_ - 1]) + float(equasion[key_ + 1])
                equasion.pop(key_)
                equasion.pop(key_)
                key_ -= 2
            if key == "-":
                if explain:
                    if step == 1:
                        explanation += f"Then we'll subtract the number {float(equasion[key_ + 1])} from {float(equasion[key_ - 1])} which results in {float(equasion[key_ - 1]) - float(equasion[key_ + 1])}\n"
                    else:
                        if random.randint(0, 1) == 0:
                            explanation += f"After that we'll subtract the number {float(equasion[key_ - 1])} with {float(equasion[key_ + 1])} which results in {float(equasion[key_ - 1]) - float(equasion[key_ + 1])}\n"
                        else:
                            explanation += f"And after that we'll subtract the number {float(equasion[key_ - 1])} with {float(equasion[key_ + 1])} which will results in {float(equasion[key_ - 1]) - float(equasion[key_ + 1])}\n"
                    step += 1
                    print(explanation)
                equasion[key_ - 1] = round(float(equasion[key_ - 1]) - float(equasion[key_ + 1]), 2)
                equasion.pop(key_)
                equasion.pop(key_)
                key_ -= 2
            key_ += 1

        if explain:
            explanation += "And at last you'll end up with " + str(equasion[0])
            print(explanation)
            return explanation
        else:
            if str(equasion[0])[-2:] == ".0":
                return str(equasion[0])[:-2]
            return equasion[0]


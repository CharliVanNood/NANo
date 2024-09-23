import random
import time

class App:
    def __init__(self):
        self.name = "RandomNumberGenerator"

        print(f"          loading {self.name}")

    def run(self):
        print(f"starting {self.name}")
        time.sleep(1)
        self.numberChosen = random.randint(1, 9)
        self.guessed = False
        while not self.guessed:
            self.TRY()
        print("you guessed it!!")
        action = input("play again? (y/n): ")
        if "y" in action.lower():
            self.run()
        else:
            time.sleep(1)

    def TRY(self):
        print("choose a number between 1 and 9")
        number = input("number: ")
        if number == str(self.numberChosen):
            self.guessed = True

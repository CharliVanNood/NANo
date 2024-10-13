import random
import time

class App:
    def __init__(self, username):
        self.name = "RandomNumberGenerator"
        self.username = username

        print(f"          loading {self.name}")

    def run(self):
        print(f"starting {self.name}")
        time.sleep(1)
        self.numberChosen = random.randint(1, 9)
        self.guessed = False
        self.guesses = 0
        self.maxGuesses = 5
        print("choose a number between 1 and 9")
        while not self.guessed and self.guesses < self.maxGuesses:
            self.TRY()
        if self.guesses < self.maxGuesses:
            print(f"you guessed it in { self.guesses} tries!!")
        else:
            print(f"you're out of tries :C'")
        action = input("play again? (y/n): ")
        if "y" in action.lower():
            self.run()
        else:
            time.sleep(1)

    def TRY(self):
        number = self.chooseOption(10)
        self.guesses += 1
        if number == self.numberChosen:
            self.guessed = True
        elif number > self.numberChosen:
            print(f"the number is lower than {number}")
        else:
            print(f"the number is higher than {number}")

    def chooseOption(self, maxLength):
        while True:
            choise = input("number: ")
            for x in range(maxLength):
                if str(x + 1) == choise:
                    return x + 1

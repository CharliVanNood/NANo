import random
import time

class App:
    def __init__(self, username):
        print(username)
        self.name = "Galgje"
        self.username = username
        self.tries = 0

        print(f"          loading {self.name}")

        self.words = [
            "Elephant","Giraffe","Kangaroo","Dolphin","Penguin","Cheetah","Flamingo","Crocodile","Hedgehog",
            "Chameleon","Ostrich","Octopus","Rhinoceros","Alligator","Hummingbird","Avocado","Blueberry",
            "Croissant","Doughnut","Guacamole","Lasagna","Pineapple","Ravioli","Tiramisu","Watermelon",
            "Cheeseburger","Zucchini","Artichoke","Pomegranate","Macaroni","Argentina","Belgium","Cambodia",
            "Denmark","Ecuador","Finland","Guatemala","Honduras","Iceland","Jamaica","Kyrgyzstan","Luxembourg",
            "Madagascar","Netherlands","Portugal","Telescope","Umbrella","Microscope","Toaster","Backpack",
            "Headphones","Skateboard","Refrigerator","Binoculars","Flashlight","Waterfall","Camera","Fountain",
            "Guitar","Sunglasses","Eiffel","Pyramids","Colosseum","Stonehenge","Taj Mahal","Big Ben","Sydney Opera",
            "Great Wall","Machu Picchu","Mount Rushmore","Petra","Leaning Tower","Niagara Falls","Christ Redeemer",
            "Sphinx","Thunderstorm","Rainbow","Avalanche","Volcano","Earthquake","Waterfall","Hurricane","Blizzard",
            "Tornado","Glacier","Coral Reef","Lightning","Tsunami","Oasis","Solar Eclipse","Basketball","Volleyball",
            "Hockey","Baseball","Swimming","Skateboarding","Golf","Cricket","Snowboarding","Archery","Fencing",
            "Marathon","Weightlifting","Gymnastics","Surfing","Architect","Pharmacist","Electrician","Scientist",
            "Firefighter","Astronaut","Teacher","Veterinarian","Carpenter","Florist","Journalist","Pilot","Librarian",
            "Barista","Plumber","Turquoise","Scarlet","Lavender","Emerald","Sapphire","Burgundy","Magenta","Tangerine",
            "Periwinkle","Coral","Amber","Mint","Mustard","Cyan","Peach","Violin","Orchestra","Drums","Saxophone","Flute",
            "Trumpet","Ukulele","Harp","Clarinet","Banjo","Tambourine","Accordion","Harmonica","Xylophone","Piano",
            "Dragon","Griffin","Unicorn","Phoenix","Minotaur","Pegasus""Mermaid","Cyclops","Kraken","Sphinx","Yeti","Hydra",
            "Cerberus","Banshee","Chimera","Happiness","Frustration","Surprise","Anxiety""Compassion","Anger","Euphoria",
            "Confusion","Nostalgia","Jealousy","Contentment","Empathy","Fear","Relief","Excitement"
        ]
        self.easy = []
        self.medium = []
        self.hard = []

        for word in self.words:
            if len(word) <= 5: self.easy.append(word)
            elif len(word) <= 8: self.medium.append(word)
            else: self.hard.append(word)
        
        self.difficulty = ""

    def run(self):
        print(f"starting {self.name}")
        self.tries = self.load()

        time.sleep(1)

        print("")
        print("88")
        print("88")
        print("88")
        print("88,dPPYba,  ,adPPYYba, 8b,dPPYba,   ,adPPYb,d8 88,dPYba,,adPYba,  ,adPPYYba,")
        print("88P'    \"8a \"\"     `Y8 88P'   `\"8a a8\"    `Y88 88P'   \"88\"    \"8a \"\"     `Y8")
        print("88       88 ,adPPPPP88 88       88 8b       88 88      88      88 ,adPPPPP88")
        print("88       88 88,    ,88 88       88 \"8a,   ,d88 88      88      88 88,    ,88")
        print("88       88 `\"8bbdP\"Y8 88       88  `\"YbbdP\"Y8 88      88      88 `\"8bbdP\"Y8")
        print("                                    aa,    ,88")
        print("                                    \"Y8bbdP\"")
        print("")

        self.difficulty = ""
        print("select difficulty ( easy / medium / hard ): ")
        while self.difficulty == "":
            choise = input("difficulty: ")
            if choise == "easy": self.difficulty = "easy"
            elif choise == "medium": self.difficulty = "medium"
            elif choise == "hard": self.difficulty = "hard"
        print(f"loading words from {self.difficulty}")

        if self.difficulty == "easy": self.chosenWord = random.choice(self.easy)
        if self.difficulty == "medium": self.chosenWord = random.choice(self.medium)
        if self.difficulty == "hard": self.chosenWord = random.choice(self.hard)
        
        self.guessedCharacters = []
        self.guessedCharactersTotal = []
        self.guessed = False
        self.guesses = 0

        while not self.guessed:
            self.TRY()
        
        print(f"you guessed the word {self.chosenWord} which is correct!")
        self.tries += 1
        self.save()
        action = input("play again? (y/n): ")
        if "y" in action.lower():
            self.run()
        else:
            time.sleep(1)
    
    def TRY(self):
        self.guessedWord = ""
        for char in self.chosenWord:
            if char.lower() in self.guessedCharacters:
                self.guessedWord += char
            elif not char == " ":
                self.guessedWord += "_"
            else:
                self.guessedWord += " "
        
        if self.guessedWord == self.chosenWord:
            self.guessed = True
            return

        self.printHangman(self.guesses)
        print(self.guessedWord)

        character = input("character: ")
        if character.lower() not in self.guessedCharactersTotal:
            self.guessedCharactersTotal.append(character.lower())
            inWord = False
            for char in self.chosenWord:
                if character.lower() == char.lower():
                    self.guessedCharacters.append(character.lower())
                    inWord = True
            if not inWord:
                self.guesses += 1
        else:
            print("this character has already been guessed.")

    def save(self):
        try:
            with open(f"applications/{self.name}/users.txt", "r") as f:
                data = f.read()
                data = data.replace(" ", "").split("\n")
                rows = ""
                for row in data:
                    if row == "": continue
                    if row.split(":")[0] == self.username:
                        rows += row.split(":")[0] + ": " + str(self.tries) + "\n"
                    else:
                        rows += row + "\n"
                with open(f"applications/{self.name}/users.txt", "w") as f:
                    f.write(rows)
                print("saved data")
        except:
            print("save data not found")
            with open(f"applications/{self.name}/users.txt", "w") as f:
                f.write(f"{self.username}: 0")
            return 0
    
    def load(self):
        try:
            with open(f"applications/{self.name}/users.txt", "r") as f:
                data = f.read()
                data = data.replace(" ", "").split("\n")
                print("loaded file")
                rows = data
                points = 0
                for row in rows:
                    if row.split(":")[0] == self.username:
                        points = int(row.split(":")[1])
                return points
        except:
            print("save data not found")
            with open(f"applications/{self.name}/users.txt", "w") as f:
                f.write(f"{self.username}: 0")
            return 0
    
    def printHangman(self, tries):
        if tries == 0:
            print("  _______")
            print(" |/      |")
            print(" |")
            print(" |")
            print(" |")
            print(" |")
            print(" |")
            print("_|___")
        elif tries == 1:
            print("  _______")
            print(" |/      |")
            print(" |      (_)")
            print(" |")
            print(" |")
            print(" |")
            print(" |")
            print("_|___")
        elif tries == 2:
            print("  _______")
            print(" |/      |")
            print(" |      (_)")
            print(" |       |")
            print(" |       |")
            print(" |")
            print(" |")
            print("_|___")
        elif tries == 3:
            print("  _______")
            print(" |/      |")
            print(" |      (_)")
            print(" |      \|")
            print(" |       |")
            print(" |")
            print(" |")
            print("_|___")
        elif tries == 4:
            print("  _______")
            print(" |/      |")
            print(" |      (_)")
            print(" |      \|/")
            print(" |       |")
            print(" |")
            print(" |")
            print("_|___")
        elif tries == 5:
            print("  _______")
            print(" |/      |")
            print(" |      (_)")
            print(" |      \|/")
            print(" |       |")
            print(" |      /")
            print(" |")
            print("_|___")
        else:
            print("  _______")
            print(" |/      |")
            print(" |      (_)")
            print(" |      \|/")
            print(" |       |")
            print(" |      / \\")
            print(" |")
            print("_|___")

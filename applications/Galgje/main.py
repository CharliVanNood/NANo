import random
import time

class App:
    def __init__(self):
        self.name = "Galgje"

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

    def run(self):
        print(f"starting {self.name}")
        time.sleep(1)
        self.chosenWord = random.choice(self.words)
        self.guessedCharacters = []

        self.guessed = False

        while not self.guessed:
            self.TRY()
        
        print(f"you guessed the word {self.chosenWord} which is correct!")
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

        print(self.guessedWord)

        character = input("character: ")
        for char in self.chosenWord:
            if character.lower() == char.lower():
                self.guessedCharacters.append(character.lower())

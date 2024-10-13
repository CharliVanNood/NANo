import random
import time

class App:
    def __init__(self, username):
        self.name = "NANoDungeon"
        self.username = username
        print(f"          loading {self.name}")

        self.actions = [
            ["You find a broken sign\n(1): You pick up the sign.\n(2): You stomp on the sign\n(3): you do nothing and walk on", [
                ["as you pick up the sign you find a hole under it filled with shiney stones, you take one +1 amethist", "amethist"], 
                ["you quickly find out this wasn't the best idea, you fall in a hole the sign was convering and take one damage", "1damage"], 
                ["nothing happened, the sign can't move on it's own", ""]]
            ], ["You see a golden necklace laying on the side of the road\n(1): You pick it up.\n(2): you do nothing and walk on", [
                ["as you pick up the necklace a horde of bandits run up to you and steal a random item", "1itemTake"], 
                ["as you walk on you see a horde of bandits waiting behind a bush, luckily you avoided them", ""]]
            ]
        ]
        self.inventory = []
        self.health = 10

    def run(self):
        print(f"starting {self.name}")
        time.sleep(1)
        print("You wake up in a lush green field as you hear birds chirping in the distance.")
        print("As you're waking up you're starting to question where you are, and start wandring.")
        print("Everything seems to be going well untill you hear a loud screach.")
        self.takeStep()
    
    def takeStep(self):
        while True:
            healthBar = '#' * self.health + "_"  * (10 - self.health)
            print(f"health: {healthBar}")
            randomAction = random.choice(self.actions)
            print(randomAction[0])
            action = self.chooseOption(len(randomAction[1]))
            print("")
            print(randomAction[1][action][0])
            self.giveItems(randomAction[1][action][1])
            print("")
            time.sleep(3)
    
    def chooseOption(self, maxLength):
        while True:
            choise = input("I choose option: ")
            for x in range(maxLength):
                if str(x + 1) == choise:
                    return x
                
    def giveItems(self, item):
        if item == "": return
        elif item == "1damage": self.health -= 1
        elif item == "1itemTake":
            if len(self.inventory) > 0:
                itemTaken = random.choice(self.inventory)
                itemIndex = self.inventory.index(itemTaken)
                self.inventory.pop(itemIndex)
                print(f"the item {itemTaken} has been taken")
            else:
                print("you have nothing on you and have nothing to lose")
        else: self.inventory.append(item)
import os
import importlib
import keyboard
import time

class Launcher:
    def __init__(self):
        print("          starting launcher")

        self.applications = []
        self.loadApplications()

        self.selected_idx = 0

        print("[ \033[92m  OK \033[0m ] started launcher")
        time.sleep(0.5)

        self.drawGameMenu()
        while True:
            self.checkInput()

    def loadApplications(self):
        print("          loading applications")
        arr = os.listdir('./applications/')
        for app_ in arr:
            try:
                app = importlib.import_module(f'applications.{app_}.main')
                application = app.App()
                self.applications.append([app_, application])
                print(f"[ \033[92m  OK \033[0m ] loaded in {app_}")
            except:
                print(f"[ \033[91mERROR\033[0m ] failed to load in {app_}")
        self.applications.append(["exit", None])

    def drawGameMenu(self):
        os.system('cls' if os.name == 'nt' else 'clear')

        print("")
        print("###   ###     ###     ###   ###    \033[92m#####\033[0m  ")
        print("####  ###   ### ###   ####  ###   \033[92m#######\033[0m ")
        print("##### ###  ###   ###  ##### ###  \033[92m###   ###\033[0m")
        print("### #####  #########  ### #####  \033[92m###   ###\033[0m")
        print("###  ####  #########  ###  ####   \033[92m#######\033[0m ")
        print("###   ###  ##     ##  ###   ###    \033[92m#####\033[0m  ")
        print("")
        print("Select Application ________________________")

        for idx, option in enumerate(self.applications):
            if idx == self.selected_idx:
                print(f"> {option[0]}")
            else:
                print(f"  {option[0]}")

    def checkInput(self):
        if keyboard.is_pressed('up'):
            self.selected_idx = (self.selected_idx - 1) % len(self.applications)
            self.drawGameMenu()
            keyboard.read_event()

        elif keyboard.is_pressed('down'):
            self.selected_idx = (self.selected_idx + 1) % len(self.applications)
            self.drawGameMenu()
            keyboard.read_event()

        elif keyboard.is_pressed('enter'):
            if self.selected_idx == len(self.applications) - 1:
                print("Exiting...")
                exit()
            print(f"You selected '{self.applications[self.selected_idx][0]}'")
            self.drawGameMenu()
    
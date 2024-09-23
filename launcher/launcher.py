import os
import importlib

class Launcher:
    def __init__(self):
        print("          starting launcher")

        self.applications = []

        self.loadApplications()

        print("[ \033[92m  OK \033[0m ] started launcher")
        print("")
        print("###   ###     ###     ###   ###    \033[92m#####\033[0m  ")
        print("####  ###   ### ###   ####  ###   \033[92m#######\033[0m ")
        print("##### ###  ###   ###  ##### ###  \033[92m###   ###\033[0m")
        print("### #####  #########  ### #####  \033[92m###   ###\033[0m")
        print("###  ####  #########  ###  ####   \033[92m#######\033[0m ")
        print("###   ###  ##     ##  ###   ###    \033[92m#####\033[0m  ")
        print("")

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

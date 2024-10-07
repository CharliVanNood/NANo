import random
import time
import wikipedia as wp
from bs4 import BeautifulSoup as BS
from urllib.request import urlopen
import re

class App:
    def __init__(self, username):
        self.name = "QuickSearch"
        self.username = username

        print(f"          loading {self.name}")

    def run(self):
        print(f"starting {self.name}")
        time.sleep(1)
        print("")
        search = input("search word (n to close): ")

        if search == "n":
            return
        
        searchQuery = search.lower().replace("?", "").replace(".", "").split(" ")
        query = ""
        for key in searchQuery:
            query += key + " "
        print(searchQuery)

        queryList = wp.search(query, results = 10)
        if len(queryList) == 0:
            print("No Results found")
            self.run()

        foundResult = False
        while not foundResult:
            weights = []
            for key in queryList:
                weight = 0
                for word in searchQuery:
                    if word in key.lower().replace("(", "").replace(")", "").split(" "):
                        weight += 1 / len(key.lower().split(" "))
                    elif word in key.lower():
                        weight += 0.25 / len(key.lower().split(" "))
                weights.append(weight)
            print(weights)
            maxWeight = max(weights)
            indexWeight = weights.index(maxWeight)
            print(queryList)
            print("searching for " + str(queryList[indexWeight].replace(" ", "%20")))
            print("")

            result_ = self.searchTerm(queryList[indexWeight].replace(" ", "%20"), queryList)
            if result_[0] != "_not found_":
                foundResult = True
                print(result_[0])
                self.run()
            else:
                queryList.remove(queryList[indexWeight])

        print("No Results found")
        self.run()

    def searchTerm(self, term, queryList):
        html = urlopen(f'https://en.wikipedia.org/wiki/{term}')
        elem = BS(html, features="html.parser").find('div', attrs={"class": "mw-content-ltr mw-parser-output"})
        elems = elem.findAll('p', attrs={'class': None})
        for elem_ in elems:
            elem__ = re.sub('<[^>]+>', '', elem_.text)
            elem__ = re.sub('\[[^>]+\]', '', elem__)
            if len(elem__.split(" ")) > 20:
                return [elem__, False]
        print("No Results found")
        self.run()

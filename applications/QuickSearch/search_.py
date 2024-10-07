import wikipedia as wp
from bs4 import BeautifulSoup as BS
from urllib.request import urlopen
import re

from responses.search import searchData


def searchTerm(term, queryList):
    html = urlopen(f'https://en.wikipedia.org/wiki/{term}')
    elem = BS(html, features="html.parser").find('div', attrs={"class": "mw-content-ltr mw-parser-output"})
    elems = elem.findAll('p', attrs={'class': None})
    for elem_ in elems:
        elem__ = re.sub('<[^>]+>', '', elem_.text)
        elem__ = re.sub('\[[^>]+\]', '', elem__)
        if len(elem__.split(" ")) > 20:
            return [elem__, False]
    return ["_not found_", False]


def search_(message, users, save, Embed, text):
    sequenceIn = text.replace(".", " . ").replace("!", " ! ").replace("?", " ? ").lower().split(" ")
    weights = []
    for key in searchData:
        weight = 0
        for word in sequenceIn:
            if word in key[0]:
                weight += 1
        weights.append(weight)
    maxWeight = max(weights)
    if maxWeight > 3:
        indexWeight = weights.index(maxWeight)
        return [searchData[indexWeight][1], False]

    print("searching for new data")
    searchQuery = text.lower().replace("?", "").replace(".", "").split(" ")[2:]
    query = ""
    for key in searchQuery:
        query += key + " "
    print(searchQuery)

    queryList = wp.search(query, results = 10)
    if len(queryList) == 0:
        return ["_not found_", False]

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

        result_ = searchTerm(queryList[indexWeight].replace(" ", "%20"), queryList)
        if result_[0] != "_not found_":
            foundResult = True
            return result_
        else:
            queryList.remove(queryList[indexWeight])

    return ["_not found_", False]
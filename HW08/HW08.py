#!/usr/bin/env python3
"""
Georgia Institute of Technology - CS1301
HW08 - APIs
"""

import requests

"""
Function Name: meetNewPeople()
Parameters: house (str)
Returns: list of people (list)
"""

def meetNewPeople(house):
    apiKey = "$2a$10$4B95LnHHtY4Rwoe2Ah34IO1urSSipQYyIhfwVvOYFAoqHaAEnOg7K"
    baseUrl = "https://www.potterapi.com/v1/"
    url = baseUrl + "characters" + "?key=" + apiKey
    r = requests.get(url)
        
    theData = r.json()
    outputData = []
    for x in theData:
        if "house" in x and x["house"] == house:
            if "bloodStatus" in x and x["bloodStatus"] == "pure-blood":
                if "deathEater" in x and x["deathEater"] == False:
                    outputData.append(x["name"])
    return outputData

"""
Function Name: matchingStudents()
Parameters: character name (str)
Returns: list of students (list)
"""

def matchingStudents(charName):
    apiKey = "$2a$10$4B95LnHHtY4Rwoe2Ah34IO1urSSipQYyIhfwVvOYFAoqHaAEnOg7K"
    baseUrl = "https://www.potterapi.com/v1/"
    url = baseUrl + "characters" + "?key=" + apiKey
    r = requests.get(url)
      
    theData = r.json()
    outputData = []
    temp = 0
    for x in theData:
        if "name" in x and x["name"] == charName:
            temp = x
    for x in theData:
        if "name" in x and x["name"] == charName:
            continue
        if "bloodStatus" in x and x["bloodStatus"] == temp["bloodStatus"]:
            if "house" in x and x["house"] == temp["house"]:
                if "role" in x and x["role"] == "student":
                    outputData.append(x["name"])
    return outputData

"""
Function Name: similarCharacters()
Parameters: movieID1 (str), movieID2 (str)
Returns: number of people (int)
"""

def similarCharacters(movieID1, movieID2):
    baseUrl = "https://swapi.dev/api/"
    url = baseUrl + "films/" + movieID1
    r = requests.get(url)

    theData = r.json()
    if "detail" in theData and theData["detail"] == "Not found":
        return 0
    name1 = theData["characters"]
    
    url2 = baseUrl + "films/" + movieID2
    r2 = requests.get(url2)
    theData = r2.json()
    if "detail" in theData and theData["detail"] == "Not found":
        return 0
    name2 = theData["characters"]
    counter = 0
    for x in name1:
        if x in name2:
            counter += 1
    return counter

"""
Function Name: spaceDrifting()
Parameters: passengers(int), max price(int)
Returns: list of valid starships (list)
"""

def spaceDrifting(passengers, maxPrice):
    baseUrl = "https://swapi.dev/api/"
    url = baseUrl + "starships/"
    r = requests.get(url)

    outputData = []
    theData = r.json()
    for x in theData["results"]:
        if x["cost_in_credits"].isdigit() and int(x["cost_in_credits"]) < maxPrice:
            if x["passengers"].isdigit() and int(x["passengers"]) >= passengers:
                outputData.append((x["name"], x["manufacturer"]))
    return outputData

"""
Function Name: perfectMatch()
Parameters: list of candidates (list)
Returns: list of potential matches (list)
"""

def perfectMatch(candidates):
    baseUrl = "https://swapi.dev/api/"
    url = baseUrl + "people/"
    r = requests.get(url)

    for x in candidates:
        if x == "Luke Skywalker" or x == "Darth Vader":
            candidates.remove(x)
    outputData = []
    theData = r.json()

    for x in theData["results"]:
        if x["name"] in candidates:
            if x["height"].isdigit() and int(x["height"]) >= 180:
                if x["gender"] == "male":
                    outputData.append(x["name"])
    return outputData

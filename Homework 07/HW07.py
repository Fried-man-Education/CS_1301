#!/usr/bin/env python3
"""
Georgia Institute of Technology - CS1301
HW07 - File I/O & CSV
"""

"""
Function Name: findCuisine()
Parameters: filename (str), cuisine (str)
Returns: list of restaurants (list)
"""

def findCuisine(filename, cuisine):
    f = open(filename, "r")
    data = f.read().split('\n\n')
    f.close()
    target = []
    for x in data:
        if cuisine == x.split('\n')[1]:
            target.append(x.split('\n')[0])
    return target
    

"""
Function Name: restaurantFilter()
Parameters: filename (str)
Returns: dictionary that maps cuisine type (str) to a 
list of restaurants of the same cuisine type (list)
"""

def restaurantFilter(filename):
    f = open(filename, "r")
    data = f.read().split('\n\n')
    f.close()
    target = {}
    for x in data:
        if x.split('\n')[1] in target:
            target[x.split('\n')[1]].append(x.split('\n')[0])
        else:
            target[x.split('\n')[1]] = [x.split('\n')[0]]
    return target

"""
Function Name: createDirectory()
Parameters: filename (str), output filename (str)
Returns: None (NoneType)
"""

def createDirectory(inputfile, outputfile):
    f = open(inputfile, "r")
    data = f.read().split('\n\n')
    f.close()
    target = {}
    if str(data).strip() == "['']": #Case: empty contents
        f = open(outputfile, "w")
        f.write("Restaurant Directory\n\nFast Food\n\nSit-down")
        f.close()
        return None
    for x in data:
        newEntry = str(x.split('\n')[0]).strip() + " - " + str(x.split('\n')[1]).strip()
        if x.split('\n')[2] in target:
            target[x.split('\n')[2]].append(newEntry)
        else:
            target[x.split('\n')[2]] = [newEntry]
    dictConvert = "Restaurant Directory\n"
    for x in sorted(target):
        if x != "Fast Food" and x != "Sit-down":
            continue
        dictConvert += "\n" + x + "\n"
        target[x].sort()
        for num in range(0, len(target[x])):
            dictConvert += str(num + 1) + ". " + target[x][num] + "\n"
    f = open(outputfile, "w")
    f.write(dictConvert.strip())
    f.close()
    return None

"""
Function Name: infectedPercentage()
Parameters: country list(list), filename(str)
Returns: country and percentage (tuple)
"""

def infectedPercentage(countryList, filename):
    f = open(filename, "r")
    data = f.read().split('\n')
    f.close()
    data = data[1:]
    dictData = {}
    for x in range(0, len(data)):
        dictData[data[x].split(',')[0]] = data[x].split(',')[1:]
    target = None
    for x in countryList:
        if not target or int(dictData[x][1]) / int(dictData[x][0]) > int(dictData[target][1]) / int(dictData[target][0]):
            target = x
    if not target:
        return target
    return(target, round(int(dictData[target][1]) / int(dictData[target][0]) * 100, 2))
"""
Function Name: countryStatus()
Parameters: country list (list), filename(str)
Returns: risk dictionary (dict)
"""

def countryStatus(countryList, filename):
    f = open(filename, "r")
    data = f.read().split('\n')
    f.close()
    data = data[1:]
    dictData = {}
    for x in range(0, len(data)):
        dictData[data[x].split(',')[0]] = data[x].split(',')[1:]
    target = {'Low risk': [], 'Medium risk': [], 'High risk': []}
    for key, value in dictData.items():
        if not key in countryList:
            continue
        CountryValue = int(value[1]) / int(value[0])
        if CountryValue <= .25:
            target['Low risk'].append(key)
        elif CountryValue <= .65:
            target['Medium risk'].append(key)
        else:
            target['High risk'].append(key)
    return target

"""
Function Name: compareRisk()
Parameters: country to compare (str), country list (list), filename(str)
Returns: compared countries (list)
"""

def compareRisk(country, countryList, filename):
    f = open(filename, "r")
    data = f.read().split('\n')
    f.close()
    data = data[1:]
    dictData = {}
    for x in range(0, len(data)):
        dictData[data[x].split(',')[0]] = data[x].split(',')[1:]
    target = []
    for key, value in dictData.items():
        if not key in countryList:
            continue
        if int(value[1]) > int(dictData[country][1]) and int(value[0]) < int(dictData[country][0]):
            target.append(key)
    if target == []:
        return "No countries"
    return target

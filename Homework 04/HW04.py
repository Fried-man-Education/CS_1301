"""
Georgia Institute of Technology - CS1301
HW04 - Strings, Indexing and Lists
"""

#########################################

"""
Function Name: findMax()
Parameters: a caption list of numbers (list), start index (int), stop index (int)
Returns: highest number (int)
"""
def findMax(theNumbersMason, theStart, theEnd):
    highscore = theNumbersMason[theStart]
    for x in theNumbersMason[theStart:theEnd+1]:
        if x > highscore:
            highscore = x
    return highscore

#########################################

"""
Function Name: fruitPie()
Parameters: list of fruits (list), minimum quantity (int)
Returns: list of fruits (list)
"""
def fruitPie(theFruit, theMin):
    acceptableFruit = []
    for x in range(0, len(theFruit)):
        if x % 2 != 0 and theFruit[x] >= theMin:
            acceptableFruit.append(theFruit[x-1])
    return acceptableFruit

#########################################

"""
Function Name: replaceWord()
Parameters: initial sentence (str), replacement word (str)
Returns: corrected sentence (str)
"""
def replaceWord(sentence, word):
    segments = sentence.split()
    sentence = ""
    for x in segments:
        if len(x) >= 5:
            sentence = sentence + word + " "
        else:
            sentence = sentence + x + " "
    return sentence[0:len(sentence) - 1]
    

#########################################

"""
Function Name: highestSum()
Parameters: list of strings (strings)
Returns: index of string with the highest sum (int)
"""
def highestSum(theStrings):
    high = [0, 0] # index, score
    for x in range(0, len(theStrings)):
        sum = 0
        for y in theStrings[x]:
            if y.isdigit():
                sum = sum + int(y)
        if sum > high[1]:
            high = [x, sum]
    return high[0]
    

#########################################

"""
Function: sublist()
Parameters: alist (list), blist (list)
Returns: True or False (`boolean`)
"""
def sublist(aList, bList):
    bLength = len(bList)
    if bLength == 0:
        return True
    for x in aList:
        if x == bList[0]:
            if len(bList) == 1:
                return True
            bList = bList[1:len(bList)]
        else:
            if bLength != len(bList):
                return False
    return False

#!/usr/bin/env python3
"""
Georgia Institute of Technology - CS1301
HWEC - Extra Credit Problems
"""

"""
Function Name: validParentheses()
Parameters: a string with parentheses (str)
Returns: valid or not (bool)
"""

def validParentheses(inputStr):
    return inputStr.count('(') == inputStr.count(')') and inputStr.count('[') == inputStr.count(']')

"""
Function Name: bubbleSort()
Parameters: a list (list), the list's length (int)
Returns: None (NoneType)
"""

def bubbleSort(inputList, listLen):
    if listLen <= 1:
        return
    for i in range(listLen - 1):
        if inputList[i] > inputList[i + 1]:
            inputList[i], inputList[i + 1] = inputList[i + 1], inputList[i]
    bubbleSort(inputList, listLen - 1)

"""
Function Name: groupAnagrams()
Parameters: list of strings (list)
Returns: grouped anagrams (dict)
"""

def groupAnagrams(listStr):
    tempDic = {}
    for x in listStr:
        x = str(x)
        if ''.join(sorted(x)) in tempDic:
            tempList = tempDic[''.join(sorted(x))]
            tempList.append(x)
            tempDic[''.join(sorted(x))] = tempList
        else:
            tempDic[''.join(sorted(x))] = [x]
    return tempDic

"""
Problem Name: Winter Break
"""

class Friend:
    def __init__(self, name, schedule):
        self.name = name
        self.schedule = schedule

    def addActivity(self, inputTup):
        if not inputTup[0] in self.schedule:
            self.schedule[inputTup[0]] = inputTup[1]
        else:
            return "Not possible"

class Planner:
    def __init__(self, friendsList):
        self.friendsList = friendsList

    def freeTime(self):
        temp = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        for x in self.friendsList:
            for y in x.schedule.keys():
                if y in temp:
                    temp.remove(y)
        if len(temp) == 0:
            return "No one is free"
        return temp

    def plans(self, inputDay):
        days = {}
        for x in self.friendsList:
            if inputDay in x.schedule and x.schedule[inputDay] in days:
                tempList = days[x.schedule[inputDay]]
                tempList.append(x.name)
                days[x.schedule[inputDay]] = tempList
            else:
                days[x.schedule[inputDay]] = [x.name]
        return days

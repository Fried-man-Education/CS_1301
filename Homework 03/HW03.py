import math

"""
Georgia Institute of Technology - CS1301
HW03 - Iteration
"""

#########################################

"""
Function Name: movieNight()
Parameters: a caption (str)
Returns: the fixed caption (str)
"""
def movieNight(caption):
    tempString = ''
    for x in caption:
        if not x.isdigit():
            tempString = tempString + x
    return tempString

#########################################

"""
Function Name: iceCream()
Parameters: flavor (str), number of vowels (int)
Returns: a sentence (str)
"""
def iceCream(flavor, vowels):
    amountVowels = 0
    flavor = flavor.lower()
    for x in flavor:
        if x in "aeiou":
            amountVowels = amountVowels + 1
    if amountVowels > vowels:
        return "Yes, " + flavor + " ice cream has more than " + str(vowels) + " vowels!"
    return "No, " + flavor + " ice cream doesn't have more than " + str(vowels) + " vowels!"

#########################################

"""
Function Name: dreamCar()
Parameters: car price (float), bank balance(float), interest rate (float)
Returns: number of years (int)
"""
def dreamCar(price, balance, rate):
    return math.ceil(math.log(price/balance)/ math.log(1 + rate / 100))

#########################################

"""
Function Name: battleship()
Parameters: board size (int)
Returns: None (NoneType)
"""
def battleship(size):
    for y in range(size):
        for x in range(size):
            print(str(chr(97 + y)) + str(x + 1), end='')
            if x != size - 1:
                print(" ", end= '')
        print()

#########################################

"""
Function: tennisMatch()
Parameters: player 1 (str), player 2 (str), match record (str)
Returns: winner (str)
"""
def tennisMatch(p1, p2, record):
    score1 = 0
    score2 = 0
    for game in record.split('-'):
        temp1 = 0
        temp2 = 0
        for x in game:
            if x == '1':
                temp1 = temp1 + 1
            elif x == '2':
                temp2 = temp2 + 1
        if temp1 > temp2:
            score1 = score1 + 1
        elif temp2 > temp1:
            score2 = score2 + 1
    if score1 > score2:
        return p1 + " won! The score was " + str(score1) + "-" + str(score2) + "."
    if score1 < score2:
        return p2 + " won! The score was " + str(score1) + "-" + str(score2) + "."
    return "It's a tie!"

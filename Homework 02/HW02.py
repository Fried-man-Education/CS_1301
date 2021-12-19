

"""
Georgia Institute of Technology - CS1301
HW02 - Conditionals
"""

#########################################

"""
Function Name: skillLevel()
Parameters: passRate (int)
Returns: "Beginner" or "Moderate" or "Advanced" (str)
"""
def skillLevel(passRate):
    if(passRate <= 25):
        return 'Beginner'
    elif(passRate <= 75):
        return 'Moderate'
    else:
        return 'Advanced'

#########################################

"""
Function Name: bookStore()
Parameters: item (str), walletAmount (float), quantity (int)
Returns: moneyLeftOver (float)
"""
def bookStore(item, walletAmount, quantity):
    if(item == 'Shirt'):
        item = 15.50
    elif(item == 'Lanyard'):
        item = 4.25
    elif(item == 'Sweatshirt'):
        item = 25.00
    else:
        item = 10.50
    total = round(item * quantity, 2)
    if(walletAmount > total):
        return round(walletAmount - total, 2)
    else:
        return 'Not enough money!'

#########################################

"""
Function Name: dinnerPlans()
Parameters: distance (int), hungerLevel (str)
Returns: transportMode (str)
"""
def dinnerPlans(distance, hungerLevel):
    if(hungerLevel == 'Very Hungry'):
        if(distance > 1):
            return 'Uber'
        else:
            return 'Walk'
    elif(hungerLevel == 'Hungry'):
        if(distance > 3):
            return 'Uber'
        else:
            return 'Walk'
    elif(hungerLevel == 'Slightly Hungry'):
        if(distance > 5):
            return 'Uber'
        else:
            return 'Walk'
    else:
        if(distance > 7):
            return 'Uber'
        else:
            return 'Walk'

#########################################

"""
Function Name: weekendTrip()
Parameters: distance (float), speed (float), freeTime (float)
Returns: transportMode (str)
"""
def weekendTrip(distance, speed, freeTime):
    timePercent = (distance / speed) / freeTime * 100
    if(timePercent > 20):
        return 'Going to this destination would take too much time.'
    else:
        if(speed <= 15):
            return 'walking'
        elif(speed <= 20):
            return 'biking'
        else:
            return 'driving'

#########################################

"""
Function Name: textFriends()
Parameters: distance (float), speed (float), freeTime (float), numSnacks (int), numFriends (int)
Returns: textMsg (str)
"""
def textFriends(distance, speed, freeTime, numSnacks, numFriends):
    response = weekendTrip(distance, speed, freeTime)
    if(response == 'Going to this destination would take too much time.'):
        return response
    else:
        return 'If each of us gets ' + str(numSnacks // numFriends) + ' snack(s), there will be ' + str(numSnacks % numFriends) + ' left. I will be ' + response + ', who else is doing the same?'

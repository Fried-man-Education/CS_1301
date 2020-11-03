 #!/usr/bin/env python3
"""
Georgia Institute of Technology - CS1301
HW09 - Recursion
"""

"""
Function Name: pickyEater()
Parameters: food list (list)
Returns: number of food items that can be eaten (int)
"""

def pickyEater(food):
    goodie = 0
    if len(food) == 0:
        return goodie
    elif len(food[0]) % 2 == 0 and food[0] != "":
        goodie = 1
    return goodie + pickyEater(food[1:])

"""
Function Name: inviteFriends()
Parameters: list of invitees (list)
Returns: flattened list of all invitees (list)
"""

def inviteFriends(invitees):
    if type(invitees) == list:
        if len(invitees) == 0:
            return None
        if len(invitees) > 1:
            firstTemp = inviteFriends(invitees[0])
            nextTemp = inviteFriends(invitees[1:])
            if nextTemp == None:
                return firstTemp
            if firstTemp == None:
                return nextTemp
            return firstTemp + nextTemp
        return inviteFriends(invitees[0])
    return [invitees]
          
"""
Function Name: friendsgiving()
Parameters: stores (list), budget (float), maxDistance (int)
Returns: price of sauce at each store (dict)
"""

def friendsgiving(stores, budget, maxDistance):
    storeDict = {}
    if len(stores) == 0:
        return storeDict
    if stores[0][1] < budget and stores[0][2] < maxDistance:
        storeDict[stores[0][0]] = stores[0][1]
    temp = friendsgiving(stores[1:], budget, maxDistance)
    if temp != {}:
        return {**temp, **storeDict}
    return storeDict

"""
Function Name: palindrome()
Parameters: string (str), guess (int)
Returns: Whether the string contains a number of palindromes (bool)
"""

def palindrome(text, guess):
    if len(text) < 3:
        if guess == 0:
            return True
        return False
    if text[0] == text[2] and text[0] != text[1]:
        return palindrome(text[1:], guess - 1)
    return palindrome(text[1:], guess)

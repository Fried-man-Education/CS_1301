"""
Georgia Institute of Technology - CS1301
HW01 - Functions and Expressions
"""

#########################################

"""
Function Name: listen()
Parameters: N/A
Returns: None
"""
def listen():
    songs = int(input("How many songs did you listen to? "))
    podcasts = int(input("How many podcasts did you listen to? "))
    totalMinutes = songs * 3 + podcasts * 25
    print("By listening to " + str(songs) + " songs and " + str(podcasts) + " podcasts, you have spent " + str(totalMinutes // 60) + " hours and " + str(totalMinutes % 60) + " minutes on Spotify.")

#########################################

"""
Function Name: dominosTime()
Parameters: N/A
Returns: None
"""
def dominosTime():
    pizzas = int(input("How many pizzas do you want? "))
    pasta = int(input("How many orders of pasta do you want? "))
    wings = int(input("How many orders of chicken wings do you want? "))
    total = pizzas * 12 + pasta * 6 + wings * 8
    print("By ordering " + str(pizzas) + " pizzas, " + str(pasta) + " orders of pasta, and " + str(wings) + " orders of chicken wings, your order total comes to $" + str(total) + ".")

#########################################

"""
Function Name: tipAndSplit()
Parameters: N/A
Returns: None
"""
def tipAndSplit():
    total = int(input("What was the order total? "))
    percentage = int(input("What percentage would you like to tip? "))
    people = int(input("How many people are splitting the order? "))
    print("The driver got a tip of $" + str(round(total * (percentage / 100), 2)) + ". Each person paid $" + str(round(total * ((percentage + 100) / 100) / people, 2)) + ".")

#########################################

"""
Function Name: youtuber()
Parameters: N/A
Returns: None
"""
def youtuber():
    videos = int(input("How many videos have you made? "))
    adsense = float(input("How much do you get paid per view? "))
    views = int(input("How many views do your videos have? "))
    print("You have made $" + str(round(videos * adsense * views, 2)) + " by making YouTube videos!")

#########################################

"""
Function Name: bathBomb()
Parameters: N/A
Returns: None
"""
def bathBomb():
    radius = float(input("What is the radius of the bath bomb? "))
    print("The volume of a bath bomb with radius " + str(radius) + " is " + str(round(4 / 3 * 3.14 * radius ** 3, 2)) + ".")

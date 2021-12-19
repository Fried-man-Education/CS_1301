#!/usr/bin/env python3
"""
Georgia Institute of Technology - CS1301
HW10 - Object Oriented Programming
"""

class Room: # entire class provided
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

    def __repr__(self):
        return "Room(name: {})".format(self.name)

class Task:
    def __repr__(self): # provided
        return "Task(name: {}, isCompleted: {})".format(self.name, self.isCompleted)

    def __init__(self, name, isCompleted = False):
        self.name = name
        self.isCompleted = isCompleted

    def __eq__(self, other):
        return (self.name, self.isCompleted) == (other.name, other.isCompleted)

class Crewmate:
    def __init__(self, name, color, accessories = ()):
        self.name = name
        self.color = color
        self.accessories = accessories
        self.isAlive = True
        self.tasksDone = 0

    def doTask(self, Task):
        if Task.isCompleted:
            return "Nothing to do here."
        Task.isCompleted = True
        self.tasksDone += 1

    def vote(self, AmongUs):
        for x in AmongUs.crewmates:
	        if self.name[0] == x.name[0] and self.name != x.name and x.isAlive:
		        return x
        for x in AmongUs.impostors:
          if self.name[0] == x.name[0] and self.name != x.name and x.isAlive:
            return x

    def __repr__(self): # provided
        return "Crewmate(name: {}, color: {})".format(self.name, self.color)

    def callMeeting(self, AmongUs):
        votes = {}
        for x in AmongUs.crewmates:
            theVote = x.vote(AmongUs).name
            if theVote in votes:
                votes[theVote] = votes[theVote] + 1
            else:
                votes[theVote] = 1
        for x in AmongUs.impostors:
            theVote = x.vote(AmongUs).name
            if theVote in votes:
                votes[theVote] = votes[theVote] + 1
            else:
                votes[theVote] = 1
        highest = None
        for x in votes:
          if highest == None or votes[x] > votes[highest]:
            highest = x
        for x in AmongUs.crewmates:
          if x.name == highest:
            x.isAlive = False
            return 	"{} was not An Impostor.".format(x.name)
        for x in AmongUs.impostors:
          if x.name == highest:
            x.isAlive = False
            return "{} was An Impostor".format(x.name)
        

    def __eq__(self, other = False): # provided
        return (self.name, self.color, self.accessories) == (other.name, other.color, other.accessories)

class Impostor:
    def __init__(self, name, color, accessories = ()):
        self.name = name
        self.color = color
        self.accessories = accessories
        self.isAlive = True
        self.eliminateCount = 0

    def eliminate(self, person):
        if type(person) == type(self):
            return "They're on your team -_-"
        person.isAlive = False
        self.eliminateCount += 1

    def vote(self, AmongUs):
        for x in AmongUs.crewmates:
	        if self.name[0] == x.name[0] and self.name != x.name and x.isAlive:
		        return x
        for x in AmongUs.impostors:
          if self.name[0] == x.name[0] and self.name != x.name and x.isAlive:
            return x

    def __repr__(self): # provided
        return "Impostor(name: {}, color: {})".format(self.name, self.color)

    def __str__(self):
        return "My name is {} and I'm an impostor.".format(self.name)

    def __eq__(self, other): # provided
        return (self.name, self.color, self.accessories) == (other.name, other.color, other.accessories)

class AmongUs:
    def __init__(self, maxPlayers):
        self.maxPlayers = maxPlayers
        self.rooms = {}
        self.crewmates = []
        self.impostors = []

    def registerPlayer(self, person):
        if len(self.crewmates) + len(self.impostors) >= self.maxPlayers:
            return "Lobby is full."
        for x in self.crewmates:
            if person.name == x.name:
                return "Player with name: {} exists.".format(person.name)
        for x in self.impostors:
            if person.name == x.name:
                return "Player with name: {} exists.".format(person.name)
        if hasattr(person, 'tasksDone'):
            self.crewmates.append(person)
        else:
            self.impostors.append(person)

    def registerTask(self, newTask, newRoom):
        for x in self.rooms:
            if newTask in self.rooms[x]:
                return "This task has already been registered."
        if newRoom.name in self.rooms:
          temp = self.rooms[newRoom.name]
          temp.append(newTask)
          self.rooms[newRoom.name] = temp
        else:
          self.rooms[newRoom.name] = [newTask]

    def gameOver(self):
        aliveCrew = 0
        for x in self.crewmates:
            if x.isAlive:
                aliveCrew += 1
        if aliveCrew == 0:
            return "Defeat! All crewmates have been eliminated."
        aliveImpostors = 0
        for x in self.impostors:
            if x.isAlive:
                aliveImpostors += 1
        if aliveImpostors == 0:
            return "Victory! All impostors have been eliminated."
        return "Game is not over yet!"

    def __repr__(self): # provided
        return "AmongUs(maxPlayers: {})".format(self.maxPlayers)
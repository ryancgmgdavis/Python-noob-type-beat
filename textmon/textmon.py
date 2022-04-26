'''

Notes:
Use
    OOP
    return
    classes
    arguments
    other things that are big mode

Ideas:

save and load files

Megamon
    different bug types, each with varying stats
    can level up
        EXP
    different Megamon found in different locations
        randomly spawn
    feed and raise
        minigames for food.
    nicknames
    multiple mon(access pc)
    learn moves
    handicap with different types

Battling
    strongest/fastest attacks first
    stronger enemies when bug is depending on level

'''

import random
import json
from time import monotonic

class Megamon:
    def __init__(self, name, type, level, attack, defense, speed, hp, xp, pxp):
        self.name = name
        self.type = type
        self.level = level
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.hp = hp
        self.xp = xp
        self.pxp = pxp

    def newMon(self, name, type):
        variance = random.randint(1, 50)
        if variance <= 25:
            pass

    def levelUp(self):
        if self.xp == self.pxp:
            pass
        #for lvl in self.level:




Snail = Megamon("Snail", "water", 1, 2, 15, 1, 25, 0, 20)
Ladybug = Megamon("Ladybug", "normal", 1, 4, 5, 3, 15, 0, 20)
#Stickbug = Megamon.newMon(1, 5, 2, 6, 15, "Stickbug")
#HouseFly = Megamon.newMon(1, 3, 4, 7, 15, "House Fly")
#FireAnt = Megamon.newMon(5, 6, 4, 5, 20, "Fire Ant")
#Dragonfly = Megamon.newMon(6, 5, 3, 10, 20, "Dragonfly")
#StagBeetle = Megamon.newMon(10, 7, 7, 3, 30, "Stag Beetle")
Mantis = Megamon("Mantis", "fighting", 1, 13, 2, 8, 15, 0, 25)
#GoliathBeetle = Megamon.newMon(15, 9, 13, 4, 40, "Goliath Beetle")
#Scorpion = Megamon.newMon(16, 12, 10, 7, 30, "Scorpion")


class Game:
    def startscreen(self):
        newLoad = input("Would you like to start a NEW game, or LOAD a game? ").lower()
        if newLoad == "new":
            self.newGame()

    def newGame(self):
        starters = [Snail, Ladybug, Mantis]
        newMon = random.choice(starters)

        

    def zone1(self):
        pass

class Battle:
    def direct(self, opponent):
        battleOptions = input()

    def run(self):
        pass

    def fight(self):
        pass
    
    def pokemon(self):
        pass
 
    def bag(self):
        pass



Game().startscreen()
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
game display
    animated

Bugs
    different bug types, each with varying stats
    can level up
        EXP
    different bugs found in different locations
    feed and raise
    nicknames
    randomly spawn

Battling
    strongest/fastest attacks first
    stronger enemies when bug is stronger

minigames for food.

'''
import pygame 
import random
import json
import os

save_files = {
    "save1": False,
    "save2": False,
    "save3": False,
}

data = {
    "player_name": "null",
    #party
    "slot1": "null",
    "slot2": "null",
    "slot3": "null",
    "slot4": "null",
    "slot5": "null",
    "slot6": "null",
}

class Bug:
    def __init__(self, level, attack, defense, speed, health, name):
        self.level = level
        self.attack = attack + level**2 - level - level//2
        self.defense = defense + level**2 - level
        self.speed = speed + level
        self.health = health + self.defense + level**2 - level - level//3
        self.name = name

Snail = Bug(1, 2, 15, 1, 15, "Snail")
Ladybug = Bug(1, 4, 5, 3, 15, "Ladybug")
Stickbug = Bug(1, 5, 2, 6, 15, "Stickbug")
HouseFly = Bug(1, 3, 4, 7, 15, "House Fly")
FireAnt = Bug(5, 6, 4, 5, 20, "Fire Ant")
Dragonfly = Bug(6, 5, 3, 10, 20, "Dragonfly")
StagBeetle = Bug(10, 7, 7, 3, 30, "Stag Beetle")
PrayingMantis = Bug(11, 13, 5, 8, 25, "Praying Mantis")
GoliathBeetle = Bug(15, 9, 13, 4, 40, "Goliath Beetle")
Scorpion = Bug(16, 12, 10, 7, 30, "Scorpion")

species = [Snail, Ladybug, Stickbug, HouseFly, FireAnt, Dragonfly, StagBeetle, PrayingMantis, GoliathBeetle, Scorpion]

Snail_start = Bug(1, 2, 15, 1, 20, "Snail")
StagBeetle_start = Bug(1, 7, 7, 3, 30, "Stag Beetle")
PrayingMantis_start = Bug(1, 13, 5, 5, 25, "Praying Mantis")

starter = [Snail_start, StagBeetle_start, PrayingMantis_start]

emotion = ["happy", "angry", "nervous", "brave", "tired", "excited"]

def new_bug():
    pass

#file management
def load():
    global data
    global save_files
    fresh = input("Do you have a save file? ").lower()
    while fresh != fresh:
        if fresh != fresh:
            print("Input not understood.")
        fresh = input("Have you played before? ").lower()

    if fresh == "no":
        os.makedirs("bbdocs", exist_ok=True)

        json.dump(save_files, open("bbdocs/files.json", "w"))

        new_game()

    
    save_files = json.load(open("bbdocs/files.json"))

    data = json.load(open("bbdocs/save_file1.json"))
    print("Loaded file 1")
    start()
    
def save():
    global data
    global save_files
    save_files = json.load(open("bbdocs/files.json"))
    
    json.dump(data, open("bbdocs/save_file1.json", "w"))
    print("Saved file 1")
    
    json.dump(save_files, open("bbdocs/files.json", "w"))

    exit()


#zones
def zone_1():
    print("Bruh")
    exit()

#start
def new_game():
    json.dump(data, open("bbdocs/save_file1.json", "w"))
    save_files["save1"] = True

    print("you started a new game!")
    player_name = input("What is your name? ")
    print(f"Hello {player_name}! Welcome to the world of Pokemon!")
    data["player_name"] = player_name
    if data["slot1"] == "null":
        new_mon = random.choice(starter)
    print(f"Your starting Bug is {new_mon.name}!")
    nickname1 = input(f"What would you like to call your {new_mon.name}? ")
    new_mon.name = nickname1 
    data["slot1"] = nickname1
    print(data["slot1"] + " is feeling " + random.choice(emotion) + ".")
    save()
    zone_1()

def start():
    player_name = data["player_name"]
    print(f"Hello {player_name}! Welcome to the world of Digimon!")
    print(data["slot1"] + " is feeling " + random.choice(emotion) + ".")
    zone_1()
load()
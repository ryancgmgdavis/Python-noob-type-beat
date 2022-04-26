'''
Ideas:
--different positions on ship. 
time limits for decisions when in droid encounter
--picking up items (ex: keys, weapons, access codes)
--escape pod code is different every game
remember pacifist and destroy endings
--devmode
--cheat codes
speedrunning?
--options to fight, run from, or hide from the droid
--run or hide attemps can be unsuccessful
--ability to heal
--can heal only once
--cannot beat droid unless armor is equipped
--droid and player attacks can crit? (causing potential to lose even with armor)
scoring system
optional tasks
more alternative endings
droid can be distracted
--droid movement less predictable
--droid can seek player out

a, b = b, a
--or
temp = a
a = b
b = temp

stream = open("TITLE.py")
read_file = stream.read()
exec(read_file)
'''

import random

charpos = {
    "player": 1,
    "droidvalue": 6,
    "Phealth": 100,
    "Dhealth": 200
}

roomcheck = {
    "podcheck": False,
    "droidencounter": False,
    "healed": False,
    "devmode": False,
    "bigmode": False,    
}

pacifist = {
    "key": False,
    "podcode": False,
    "code": 0,
    "thrusters": False,
    "lauch": False,
    "goodend": False,
    "idiotend": False,
}

destroy = {
    "gun": False,
    "welder": False,
    "armor": False,
    "evilend": False,
#optional
    "goggles": False,
    "tracker": False,
}

def bigmode():
    dev = input("What do you want? ").lower()
    if dev == "key":
        pacifist["key"] = True
        print("You got the key.")
        bigmode()
    elif dev == "gun":
        destroy["gun"] = True
        print("You got the gun.")
        bigmode()
    elif dev == "welder":
        destroy["welder"] = True
        print("You got the welder.")
        bigmode()
    elif dev == "armor":
        destroy["armor"] = True
        print("You got the armor.")
        bigmode()
    elif dev == "tracker":
        destroy["tracker"] = True
        print("You got the Droid Tracker™.")
        bigmode()
    elif dev == "heal":
        charpos["Phealth"] = 100
        print("Health: 100")
        bigmode()
    elif dev == "nokill":
        charpos["Phealth"] = 99999999999
        print("Invincibility Activated")
        bigmode()
    elif dev == "kill droid":
        print("You Destroyed the Droid!")
        win()
    elif dev == "escape":
        print("You Escaped the Droid!")
        win()
    elif dev == "nothing":
        print("Suit yourself.")
    else:
        print("What are you, retarded??")
    
    

#Game screens
def replay():
    def rechoice():
        y_n = input("Do you want to play again? ").lower()
        if y_n == "y" or y_n == "yes":
            pacifist["key"] = False
            pacifist["podcode"] = False
            pacifist["code"] = 0
            pacifist["thrusters"] = False
            destroy["gun"] = False
            destroy["welder"] = False
            destroy["armor"] = False
            destroy["tracker"] = False
            destroy["goggles"] = False
            roomcheck["podcheck"] = False
            roomcheck["droidencounter"] = False
            roomcheck["healed"] = False
            roomcheck["devmode"] = False
            roomcheck["bigmode"] = False
            charpos["player"] = 1
            charpos["droidvalue"] = 6
            charpos["Phealth"] = 100
            charpos["Dhealth"] = 200
            startgame()
        elif y_n == "n" or y_n == "no":
            exit()
        else:
            print("Input not understood.")
    rechoice()

def win():
    print(" __  __    ______    __  __        __  __  __    _________   ___   ___       ")
    print("/_/\/_/\  /_____/\  /_/\/_/\      /_/\/_/\/_/\  /________/\ /__/\ /__/\      ")
    print("\ \ \ \ \ \  __ \ \ \ \ \ \ \     \ \ \ \ \ \ \ \___   __\/ \  \_ \  \ \     ")
    print(" \ \_\ \ \ \ \ \ \ \ \ \ \ \ \     \ \ \ \ \ \ \    \  \ \   \   `-\  \ \    ")
    print("  \_   _\/  \ \ \ \ \ \ \ \ \ \     \ \ \ \ \ \ \   _\  \ \__ \   _    \ \   ")
    print("    \  \ \   \ \_\ \ \ \ \_\ \ \     \ \_\ \_\ \ \ /__\  \__/\ \  \`-\  \ \  ")
    print("     \__\/    \_____\/  \_____\/      \_________\/ \________\/  \__\/ \__\/  ")
    if roomcheck["bigmode"] == True:
        print("You little cheater!")

    if pacifist["goodend"] == True:
        print("YOU UNLOCKED THE GOOD END")
    if destroy["evilend"] == True:
        print("YOU UNLOCKED THE BAD END")
    if pacifist["idiotend"] == True:
        print("YOU UNLOCKED THE IDIOT END")

    replay()

def lose():
    print(" __  __    ______    __  __        __        ______    ______    ______      ")
    print("/_/\/_/\  /_____/\  /_/\/_/\      /_/\      /_____/\  /_____/\  /_____/\     ")
    print("\ \ \ \ \ \  __ \ \ \ \ \ \ \     \ \ \     \  __ \ \ \  ___\/_ \  ___\/_    ")
    print(" \ \_\ \ \ \ \ \ \ \ \ \ \ \ \     \ \ \     \ \ \ \ \ \ \/___/\ \ \/___/\   ")
    print("  \_   _\/  \ \ \ \ \ \ \ \ \ \     \ \ \____ \ \ \ \ \ \____ \ \ \  ___\/_  ")
    print("    \  \ \   \ \_\ \ \ \ \_\ \ \     \ \/___/\ \ \_\ \ \  /__\ \ \ \ \____/\ ")
    print("     \__\/    \_____\/  \_____\/      \_____\/  \_____\/  \_____\/  \_____\/ ")
    if roomcheck["bigmode"] == True:
        print("LOL XD you can't even win with hacks on, scrub.")

    if pacifist["goodend"] == True:
        print("YOU UNLOCKED THE GOOD END")
    if destroy["evilend"] == True:
        print("YOU UNLOCKED THE BAD END")
    if pacifist["idiotend"] == True:
        print("YOU UNLOCKED THE IDIOT END")
    
    replay()

def score(points):
    tempScore = 0
    tempScore += points
    score = 0 + tempScore
    


#using the Tracker
def trackdroid():
    print("The Droid is in room " + str(charpos["droidvalue"]) + ".\n")

#battle
def battle():
    def freakycoin():
        coin = random.randint(1, 6)
        if roomcheck["devmode"] == True:
            print(f"coin: {coin}")
        if charpos["Phealth"] >= 90:
            if coin <= 4:
                print("You couldn't Escape!")
                droidattack()
                attackQ()
            else:
                print("You Escaped!")
                droid()
        elif 60 < charpos["Phealth"] < 90:
            if coin <= 3:
                print("You couldn't Escape!")
                droidattack()
                attackQ()
            else:
                print("You Escaped!")
                droid()
        elif 30 <= charpos["Phealth"] <= 60:
            if coin <= 2:
                print("You couldn't Escape!")
                droidattack()
                attackQ()
            else:
                print("You Escaped!")
                droid()
        elif charpos["Phealth"] < 30:
            if coin <= 1:
                print("You couldn't Escape!")
                droidattack()
                attackQ()
            else:
                print("You Escaped!")
                droid()

    def attackQ():
        choice2 = input("Do you want to attack the Droid again, or run? ").lower()
        if choice2 == "run":
            freakycoin()
            if charpos["Dhealth"] <= 100:
                charpos["Dhealth"] += 100
                print("The Droid repaired itself.")
                healthcheck()
        elif choice2 == "attack":
            attack()
        else:
            print("Input not understood.")
            attackQ()

    def healthcheck():
        if charpos["Phealth"] <= 0:
            charpos["Phealth"] = 0
        print("Your health:")
        print(charpos["Phealth"])
        if charpos["Dhealth"] <= 0:
            charpos["Dhealth"] = 0
        print("Droid health:")
        print(charpos["Dhealth"])
        print("")

    def droidattack():
        print("The Droid attacks!\n")
        Dcritroll = random.randint(0, 12)
        if roomcheck["devmode"] == True:
            print(f"Droid crit chance: {Dcritroll}")
        if Dcritroll >= 9:
            Dcrit = 20
            print("\nThe Droid landed a Critical hit!")
        else:
            Dcrit = 0
        if destroy["armor"] == True:
            charpos["Phealth"] -= (20 + Dcrit)
            healthcheck()
            if charpos["Phealth"] == 0:
                print("\nYou Died!")
                lose()
        elif destroy["armor"] == False:
            charpos["Phealth"] -= 35
            healthcheck()
            if charpos["Phealth"] == 0:
                print("You Died!")
                lose()

    def gun():
        print("\nYou fired at the Droid.")
        Pcritroll = random.randint(1, 12)
        if roomcheck["devmode"] == True:
            print(f"Your crit chance: {Pcritroll}")
        if Pcritroll >= 7:
            Pcrit = 15
            print("\nYou landed a Critical Hit!")
        else:
            Pcrit = 0
        charpos["Dhealth"] -= (5 + Pcrit)
        healthcheck()
        if charpos["Dhealth"] == 0:
            print("\nYou destroyed the Droid!!")
            destroy["evilend"] = True
            win()
        droidattack()
        attackQ()

    def welder():
        print("\nYou attacked the Droid with the laser welder.")
        Pcritroll = random.randint(1, 12)
        if roomcheck["devmode"] == True:
            print(f"Your crit chance: {Pcritroll}")
        if Pcritroll >= 9:
            Pcrit = 20
            print("\nYou landed a Critical Hit!")
        else:
            Pcrit = 0
        charpos["Dhealth"] -= (50 + Pcrit)
        healthcheck()
        if charpos["Dhealth"] == 0:
            print("\nYou destroyed the Droid!!")
            destroy["evilend"] = True
            win()
        droidattack()
        attackQ()

    def attack():
        if destroy["gun"] == False and destroy["welder"] == False:
            print("You don't have any Weapons!")
            droidattack()
            attackQ()
        elif destroy["gun"] and destroy["welder"] == True:
            weapon = input("Do you wan't to use the gun or the welder? ").lower()
            if weapon == "gun":
                gun()
            elif weapon == "welder":
                welder()
        elif destroy["gun"] == True:
            gun()
        elif destroy["welder"] == True:
            welder()
        else: 
            attack()

    choice = input("Do you want to fight the Droid, or try to run? ").lower()
    if choice == "run":
        roomcheck["droidencounter"] = True
        freakycoin()
    elif choice == "fight":
        roomcheck["droidencounter"] = True
        attack()


#droid's move
def droid():
    movecount = random.randint(1, 30)
    if roomcheck["devmode"] == True:
        print(f"movecount: {movecount}")

    if  charpos["player"] == 1 and charpos["droidvalue"] == 10:
        if movecount <= 10:
            charpos["droidvalue"] += 1
    elif charpos["player"] == charpos["droidvalue"] + 1:
        if movecount <= 10:
            charpos["droidvalue"] += 1
    elif charpos["player"] == charpos["droidvalue"] - 1:
        if movecount <= 10:
            charpos["droidvalue"] -= 1
        print("The Droid is nearby!\n")
    elif charpos["droidvalue"] < charpos["player"] < charpos["droidvalue"] + 6:
        if roomcheck["devmode"] == True:
            print("likely move forward")
        if 13 <= movecount <= 15:
            charpos["droidvalue"] += 0
            if roomcheck["devmode"] == True:
                print("+ 0")
        elif 8 < movecount < 20:
            charpos["droidvalue"] += 1
            if roomcheck["devmode"] == True:
                print("+ 1")
        elif movecount <= 8:
            charpos["droidvalue"] -= 1
            if roomcheck["devmode"] == True:
                print("- 1")
        elif movecount >= 20:
            charpos["droidvalue"] += 2
            if roomcheck["devmode"] == True:
                print("+ 2")
    elif charpos["droidvalue"] > charpos["player"] > charpos["droidvalue"] - 6:
        if roomcheck["devmode"] == True:
            print("likely move back")
        if 13 <= movecount <= 15:
            charpos["droidvalue"] += 0
            if roomcheck["devmode"] == True:
                print("+ 0")
        elif 8 < movecount < 20:
            charpos["droidvalue"] -= 1
            if roomcheck["devmode"] == True:
                print("- 1")
        elif movecount <= 8:
            charpos["droidvalue"] += 1
            if roomcheck["devmode"] == True:
                print("+ 1")
        elif movecount >= 20:
            charpos["droidvalue"] -= 2
            if roomcheck["devmode"] == True:
                print("- 2")
    else:
        if roomcheck["devmode"] == True:
            print("confused")
        if 14 <= movecount <= 16:
            charpos["droidvalue"] += 0
            if roomcheck["devmode"] == True:
                print("+ 0")
        elif movecount >= 17:
            charpos["droidvalue"] += 1
            if roomcheck["devmode"] == True:
                print("+ 1")
        elif movecount <= 13:
            charpos["droidvalue"] -= 1
            if roomcheck["devmode"] == True:
                print("- 1")

    if charpos["droidvalue"] >= 11:
        charpos["droidvalue"] = 1
    elif charpos["droidvalue"] <= 0:
        charpos["droidvalue"] = 10
    elif charpos["player"] == 1 and charpos["droidvalue"] == 10:
        print("The Droid is nearby!\n")
    elif charpos["player"] == (charpos["droidvalue"] + 1 or charpos["droidvalue"] + 2) or charpos["player"] == (charpos["droidvalue"] - 1 or charpos["droidvalue"] - 2):
        print("The Droid is nearby!\n")

def spotcheck():
    if charpos["player"] == charpos["droidvalue"]:
        print("The Droid found you!\n")
        battle()


#rooms
def exchange():
    x1 = charpos["player"]
    x2 = charpos["player"]
    if charpos["player"] != 1 and charpos["player"] != 10:
        x1 = charpos["player"]
        x2 = charpos["player"]
    elif charpos["player"] == 1:
        x1 = 11
        x2 = charpos["player"]
    elif charpos["player"] == 10:
        x1 = charpos["player"]
        x2 = 0
    choice = input(f"Do you want to go to room {x1 - 1}, room {x2 + 1}, or stay here? ").lower()
    if choice == "1" and (charpos["player"] == 10 or charpos["player"] == 2):
        droid()
        print("")
        control()
    elif choice == "2" and (charpos["player"] == 1 or charpos["player"] == 3):
        droid()
        print("")
        medical()
    elif choice == "3" and (charpos["player"] == 2 or charpos["player"] == 4):
        droid()
        print("")
        cafe()
    elif choice == "4" and (charpos["player"] == 3 or charpos["player"] == 5):
        droid()
        print("")
        bedroom()
    elif choice == "5" and (charpos["player"] == 4 or charpos["player"] == 6):
        droid()
        print("")
        storage()
    elif choice == "6" and (charpos["player"] == 5 or charpos["player"] == 7):
        droid()
        print("")
        engine()
    elif choice == "7" and (charpos["player"] == 6 or charpos["player"] == 8):
        droid()
        print("")
        weaponry()
    elif choice == "8" and (charpos["player"] == 7 or charpos["player"] == 9):
        droid()
        print("")
        airlock()
    elif choice == "9" and (charpos["player"] == 8 or charpos["player"] == 10):
        droid()
        print("")
        escape()
    elif choice == "10" and (charpos["player"] == 9 or charpos["player"] == 1):
        droid()
        print("")
        electrical()
    elif choice == "stay" and charpos["player"] == 1:
        droid()
        print("")
        control()
    elif choice == "stay" and charpos["player"] == 2:
        droid()
        print("")
        medical()
    elif choice == "stay" and charpos["player"] == 4:
        droid()
        print("")
        bedroom()
    elif choice == "stay" and charpos["player"] == 5:
        droid()
        print("")
        storage()
    elif choice == "stay" and charpos["player"] == 6:
        droid()
        print("")
        engine()
    elif choice == "stay" and charpos["player"] == 7:
        droid()
        print("")
        weaponry()
    elif choice == "stay" and charpos["player"] == 10:
        droid()
        print("")
        electrical()
    elif choice == "010985" and charpos["player"] == 1:
        roomcheck["devmode"] = True
        destroy["tracker"] = True
        print("**DEV MODE ENABLED**")
        print("Dev mode comes pre-installed with the Droid Tracker™ and all RandInt info.\n")
        exchange()
    elif choice.find("mode") != -1:
        roomcheck["bigmode"] = True
        print(choice.upper() + " ENABLED!!!!!!\n")
        bigmode()
        exchange()
    else:
        print("Input not understood.\n")
        exchange()

def control():
    charpos["player"] = 1
    spotcheck()
    print("You are in room 1-Control.")
    if destroy["tracker"] == True:
        trackdroid()

    if roomcheck["podcheck"] == True and pacifist["podcode"] == False:
        def deskdrawer():
            y_n = input("\nYou see the control desk. Would you like to search it? ").lower()
            if y_n == "y" or y_n == "yes":
                accesscode = random.randint(100000, 999999)
                pacifist["code"] = accesscode
                print(f"\nThe Escape Pod Launch Code is {accesscode}")
                pacifist["podcode"] = True
            elif y_n == "n" or y_n == "no":
                print("You did not search the control desk.")
            else:
                print("Input not understood.")
                deskdrawer()
        deskdrawer()

    exchange()

def medical():
    charpos["player"] = 2
    spotcheck()
    print("You are in room 2-Medical.")
    if destroy["tracker"] == True:
        trackdroid()

    if charpos["Phealth"] < 100 and roomcheck["healed"] == False:
        while charpos["Phealth"] < 100:
            print("\nYour health has depleated.")
            print(charpos["Phealth"])
            print("Would you like to restore your health?")
            y_n = input("*WARNING: THIS CAN ONLY BE DONE ONCE!* ").lower()
            if y_n == "y" or y_n == "yes":
                charpos["Phealth"] = 100
                print("\nHelth restored to 100.")
                break
            elif y_n == "n" or y_n == "no":
                print("You did not restore your health.")
                break
            else:
                print("Input not understood.")

    if roomcheck["droidencounter"] == True and destroy["armor"] == False:
        def floor():
            y_n = input("\nYou see the trapdoor for a smuggling hold on the floor. Would you like to search it? ").lower()
            if y_n == "y" or y_n == "yes":
                print("\nYou found a set of Standard UOSM Armor.")
                destroy["armor"] = True
            elif y_n == "n" or y_n == "no":
                print("You did not search the smuggling hold.")
            else:
                print("Input not understood.")
                floor()
        floor()

    exchange()

def cafe():
    charpos["player"] = 3
    spotcheck()
    print("You are in room 3-Cafe.")
    if destroy["tracker"] == True:
        trackdroid()

    cafe_opt = input("\nDo you want to go to room 2, room 4, room 8, room 9, or stay here? ").lower()
    if cafe_opt == "2":
        droid()
        print("")
        medical()
    elif cafe_opt == "4":
        droid()
        print("")
        bedroom()
    elif cafe_opt == "8":
        droid()
        print("")
        airlock()
    elif cafe_opt == "9":
        droid()
        print("")
        escape()
    elif cafe_opt == "stay":
        droid()
        print("")
        cafe()
    else:
        print("Input not understood.")
        cafe()

def bedroom():
    charpos["player"] = 4
    spotcheck()
    print("You are in room 4-Bedroom.")
    if destroy["tracker"] == True:
        trackdroid()

    if roomcheck["podcheck"] == True and pacifist["key"] == False:
        def nightstand():
            y_n = input("\nYou see your nightstand. Would you like to search it? ").lower()
            if y_n == "y" or y_n == "yes":
                print("\nYou found the Escape Pod Launch Key\n")
                pacifist["key"] = True
            elif y_n == "n" or y_n == "no":
                print("You did not search your nightstand.")
            else:
                print("Input not understood.")
                nightstand()
        nightstand()

    exchange()

def storage():
    charpos["player"] = 5
    spotcheck()
    print("You are in room 5-Storage.")
    if destroy["tracker"] == True:
        trackdroid()

    if roomcheck["droidencounter"] == True and destroy["welder"] == False:
        def tools():
            y_n = input("\nYou see various tools organized on a wall. Would you like to search them? ").lower()
            if y_n == "y" or y_n == "yes":
                print("\nYou found a laser welder.")
                destroy["welder"] = True
            elif y_n == "n" or y_n == "no":
                print("You did not search the tool wall.")
            else:
                print("Input not understood.")
                tools()
        tools()

    exchange()

def engine():
    charpos["player"] = 6
    spotcheck()
    print("You are in room 6-Engine.")
    if destroy["tracker"] == True:
        trackdroid()

    if roomcheck["podcheck"] == True and pacifist["podcode"] == True and pacifist["thrusters"] == False:
        def thrustpannel():
            y_n = input("\nYou see a control pannel. Would you like to use it? ").lower()
            if y_n == "y" or y_n == "yes":
                while roomcheck["podcheck"] == True:
                    code = int(input("ENTER ESCAPE POD LAUNCH CODE: "))
                    if code == pacifist["code"]:
                        break
                    else: 
                        print("LAUNCH CODE INCORRECT.")
                print("\nYou enabled the Escape Pod thrusters")
                pacifist["thrusters"] = True
            elif y_n == "n" or y_n == "no":
                print("You did not use the control pannel.")
            else:
                print("Input not understood.")
                thrustpannel()
        thrustpannel()

    exchange()

def weaponry():
    charpos["player"] = 7
    spotcheck()
    print("You are in room 7-Weaponry.")
    if destroy["tracker"] == True:
        trackdroid()

    if roomcheck["droidencounter"] == True and destroy["gun"] == False:
        def armory():
            y_n = input("\nYou see the Armory. Would you like to search it? ").lower()
            if y_n == "y" or y_n == "yes":
                print("\nYou found a Rifle with ammunition and Night vision goggles.\n")
                destroy["gun"] = True
                destroy["goggles"] = True
            elif y_n == "n" or y_n == "no":
                print("You did not search the Armory.")
            else:
                print("Input not understood.")
                armory()
        armory()

    exchange()

def airlock():
    charpos["player"] = 8
    spotcheck()
    print("You are in room 8-Airlock.")
    if destroy["tracker"] == True:
        trackdroid()

    def idiot1():
        y_n = input("\nYou see the Airlock. Would you like to open it? ").lower()
        if y_n == "y" or y_n == "yes":
            print("\nYou were sucked into the void of space.")
            print("That was pretty stupid of you...")
            pacifist["idiotend"] = True
            lose()
        elif y_n == "n" or y_n == "no":
            print("You did not open the Airlock.")
        else:
            print("Input not understood.")
            idiot1()
    idiot1()

    airlock_opt = input("\nDo you want to go to room 3, room 7, room 9, or stay here? ").lower()
    if airlock_opt == "3":
        droid()
        print("")
        cafe()
    elif airlock_opt == "7":
        droid()
        print("")
        weaponry()
    elif airlock_opt == "9":
        droid()
        print("")
        escape()
    elif airlock_opt == "stay":
        droid()
        print("")
        airlock()
    else:
        print("Input not understood.")
        airlock()

def escape():
    charpos["player"] = 9
    spotcheck()
    print("You are in room 9-Escape Pod.")
    if destroy["tracker"] == True:
        trackdroid()

    if roomcheck["podcheck"] == False:
        def escapepannel1():
            y_n = input("\nThere is a display screen on the Escape Pod. Would you like to read it? ").lower()
            if y_n == "y" or y_n == "yes":
                print("\nYOU NEED THE LAUNCH KEY TO USE THE ESCAPE POD")
                print("YOU NEED THE ACCESS CODE TO USE THE ESCAPE POD")
                print("YOU MUST ENABLE THE THRUSTERS TO USE THE ESCAPE POD")
                roomcheck["podcheck"] = True
            elif y_n == "n" or y_n == "no":
                print("You did not use the control pannel.")
            else:
                print("Input not understood.")
                escapepannel1()
        escapepannel1()
        
    elif pacifist["key"] == True and pacifist["podcode"] == True and pacifist["thrusters"] == True:
        def winner():
            y_n = input("You enter the Escape pod. Would you like to launch? ").lower()
            if y_n == "y" or y_n == "yes":
                print("You Escaped the Droid!")
                pacifist["goodend"] = True
                win()
            elif y_n == "n" or y_n == "no":
                print("You did not launch the Escape pod")
            else:
                print("Input not understood.")
                winner()
        winner()

    elif roomcheck["podcheck"] == True:
        def escapepannel2():
            y_n = input("\nThere is a display screen on the Escape Pod. Would you like to read it? ").lower()
            if y_n == "y" or y_n == "yes":
                print("")
                if pacifist["key"] == False:
                    print("YOU NEED THE LAUNCH KEY TO USE THE ESCAPE POD")
                if pacifist["podcode"] == False:
                    print("YOU NEED THE ACCESS CODE TO USE THE ESCAPE POD")
                if pacifist["thrusters"] == False:
                    print("YOU MUST ENABLE THE THRUSTERS TO USE THE ESCAPE POD")
                print("")
            elif y_n == "n" or y_n == "no":
                print("You did not use the control pannel.")
            else:
                print("Input not understood.")
                escapepannel2()
        escapepannel2()

    escape_opt = input("\nDo you want to go to room 3, room 8, room 10, or stay here? ").lower()
    if escape_opt == "3":
        droid()
        print("")
        cafe()
    elif escape_opt == "8":
        droid()
        print("")
        airlock()
    elif escape_opt == "10":
        droid()
        print("")
        electrical()
    elif escape_opt == "stay":
        droid()
        print("")
        escape()
    else:
        print("Input not understood.")
        escape()

def electrical():
    charpos["player"] = 10
    spotcheck()
    print("You are in room 10-Electrical.")
    if destroy["tracker"] == True:
        trackdroid()

    if roomcheck["droidencounter"] == True and destroy["tracker"] == False:
        def toolbox():
            y_n = input("\nYou see a toolbox. Would you like to search it? ").lower()
            if y_n == "y" or y_n == "yes":
                print("\nYou found a modified tracking device.")
                print("Any time you enter a room, you will be given the Droid's location.")
                destroy["tracker"] = True
            elif y_n == "n" or y_n == "no":
                print("You did not search the toolbox.")
            else:
                print("Input not understood.")
                toolbox()
        toolbox()

    exchange()


#start
def startgame():
    print("An evil droid is attacking your spaceship! You must escape your ship or defeat the Droid!\n")
    control()
startgame()
import random

bot = random.randrange(1, 4)

print("\n\n\nLet's play rock paper scissors!")

#converting input to a number
rock = 1
paper = 2
scissors = 3

#the scoreboard
win = 0
botwin = 0
tie = 0
champ = int(input("How many points should we play to? "))

while win != champ + 1 and botwin != champ + 1:
    
    if win == 0 and botwin == 0 and tie == 0:
        print("")
    elif win == champ:
        print("You win!\n\n\n")
        exit()
    elif botwin == champ:
        print("You lose!\n\n\n")
        exit()
    else:
        print("Let's play another round.\n")

    rps = input("Rock Paper Scissors SHOOT! ")
    rpsnum = 0
    if rps == "rock":
        rpsnum += 1
    elif rps == "paper":
        rpsnum += 2
    else:
        rpsnum += 3
    
    if rpsnum == bot:
        print("Tie!\n")
        tie += 1
    elif rpsnum >= bot:
        print("You won the round!\n")
        win += 1
    else:
        print("You lost the round!\n")
        botwin += 1

    print(f"Your score: {win} \nRobot score: {botwin}\n")

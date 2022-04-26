#feel_pos = "Good", "Great", "Not Bad"
#feel_neg = "BAD", "NOT GOOD", "HORRIBLE"

def menuloop():
    choice = input("What would you like to talk about?\n\nAccomplishments\nFeelings\nOther\n")
    if choice == "Accomplishments" or choice == "accomplishments":
        accomp = input("What did you accomplish today? ")
        print("Good job!")
    elif choice == "Feelings" or choice == "feelings":
        def feelloop():
            emo = input("Are you feeling good or bad today? ")
            if emo == "Good" or emo == "good":
                input("Why are you feeling good? ")
                print("That's good to hear.")
            elif emo == "Bad" or emo == "bad":
                input("Why don't you feel good? ")
                print("That's too bad.")
            else:
                print("Sorry. I didn't understand that.")
                feelloop()
        feelloop()
    #elif choice == "Other" or choice == "other":
        #other = input("What else do you want to talk about?")
    else:
        print("Sorry. I didn't understand that.")
        menuloop()
menuloop()
def yesnoloop():
    yesno = input("Is there anything else you'd like to talk about? ")
    if yesno == "Yes" or yesno == "yes":
        menuloop()
    elif yesno == "No" or yesno == "no":
        print("Goodbye.")
    else:
        print("Sorry. I didn't understand that.")
        yesnoloop()
yesnoloop()
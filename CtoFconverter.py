#look at dis. its the instructor exaple solution.

"""
File: check04_sample.py
Author: Brother Burton

Purpose: Convert degrees in Fahrenheit to Celsius.


degrees_f = float(input("What is the temperature in Fahrenheit? "))
degrees_c = (degrees_f - 32) * 5 / 9

print(f"The temperature in Celsius is {degrees_c:.1f} degrees.")
"""
# Note: I chose to abbreviate degrees_fahrenheit to degrees_f, because I decided
# that _f and _c were common, known abbreviations, and less likely to introduce
# bugs than if I tried to spell out "fahrenheit" in my code each time. But even
# in that case, I thought "degrees_f" seemed more obvious than the single
# letter variable name of "f".

#are you kiddin me?? 
#dis is baby games.
#now wach da mastah B)

#the classic opener v
print("\n\n\n")

#the big mode v
x = 1
if x != 1: 
    print("Goodbye.\n\n\n")

while x == 1:    
    while x == 1:
        option = input("Would you like to convert to Fahrenheit or Celsius? ")

        #ans_F = "Fahrenheit" and "fahrenheit" and "F" and "f"
        #ans_C = "Celsius" and "celsius" and "C" and "c"

        if option == "f":
            deg_F = float(input("What is the temperature? "))
            deg_convert_C = (deg_F - 32) * 5 / 9
            print(f"{deg_F:.2f}° F = {deg_convert_C:.2f}° C")
            break
        elif option == "c":
            deg_C = float(input("What is the temperature? "))
            deg_convert_F = (deg_C * 9 / 5) + 32
            print(f"{deg_C:.2f}° C = {deg_convert_F:.2f}° F")
            break
        else:
            print("Sorry, I didn't understand that.\n")
        
    while x == 1:
        retry = input("Would you like to run another conversion? ")

        #re_pos = "Yes" + "yes" + "Y" + "y"
        #re_neg = "No" and "no" and "N" and "n"

        if retry == "yes":
            x += 0
            break
        elif retry == "no":
            x += 1
            break
        else:
            print("Sorry, I didn't understand that.\n")

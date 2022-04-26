score = int(input("What was your test score? "))

if score >= 90:
    if score <= 93:
        print("Your letter Grade is A-!")
    else:
        print("Your letter grade is A!")
elif score >= 80:
    if score >= 87:
        print("Your letter Grade is B+!")
    elif score <= 83:
        print("Your letter Grade is B-!")
    else:
        print("Your letter grade is B!")
elif score >= 70:
    if score >= 77:
        print("Your letter Grade is C+!")
    elif score <= 73:
        print("Your letter Grade is C-!")
    else:
        print("Your letter grade is C!")
elif score >= 60:
    if score >= 67:
        print("Your letter Grade is D+.")
    elif score <= 63:
        print("Your letter Grade is D-.")
    else:
        print("Your letter grade is D.")
else:
    print("You got an F.")
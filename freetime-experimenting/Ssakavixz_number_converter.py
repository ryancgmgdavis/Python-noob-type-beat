print("\n\n\n")

x = 1
if x != 1: 
    print("Goodbye.\n\n\n")

while x == 1:
    while x == 1:
        power = int(input("Enter the number's power. (can be no bigger than 6) "))

        if power == 1:
            p1 = input("Enter the number's notation: ")
            print(f"\nbase 10 value: {p1}")
            break
        elif power == 2:
            one, two = input("Enter the number's notation: ").split()
            two10 = int(two) * 16
            base10 = two10 + int(one)
            print(f"\n{base10}")
            break
        elif power == 3:
            one, two, three = input("Enter the number's notation: ").split()
            two10 = int(two) * 16
            three10 = int(three) * 16 ** 2
            base10 = three10 + two10 + int(one)
            print(f"\n{base10}")
            break
        elif power == 4:
            one, two, three, four = input("Enter the number's notation: ").split()
            two10 = int(two) * 16
            three10 = int(three) * 16 * 16
            four10 = int(four) * 16 * 16 * 16
            base10 = four10 + three10 + two10 + int(one)
            print(f"\n{base10}")
            break
        elif power == 5:
            one, two, three, four, five = input("Enter the number's notation: ").split()
            two10 = int(two) * 16
            three10 = int(three) * 16 * 16
            four10 = int(four) * 16 * 16 * 16
            five10 = int(five) * 16 * 16 * 16 * 16
            base10 = five10 + four10 + three10 + two10 + int(one)
            print(f"\n{base10}")
            break
        elif power == 6:
            sone, two, three, four, five, six = input("Enter the number's notation: ").split()
            two10 = int(two) * 16
            three10 = int(three) * 16 * 16
            four10 = int(four) * 16 * 16 * 16
            five10 = int(five) * 16 * 16 * 16 * 16
            six10 = int(six) * 16 * 16 * 16 * 16 * 16
            base10 = six10 + five10 + four10 + three10 + two10 + int(one)
            print(f"\n{base10}")
            break
        else:
            print("Power unclear. Try again.\n")

    while x == 1:
        retry = input("Would you like to run another conversion? ")

        #re_pos = "Yes" and "yes" and "Y" and "y"
        #re_neg = "No" and "no" and "N" and "n"

        if retry == "yes":
            x += 0
            break
        elif retry == "no":
            x += 1
            break
        else:
            print("Input unclear. Try again.\n")

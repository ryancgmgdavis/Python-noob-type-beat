print("\n\n\n")

user = "cool"
password = "cooler"

attempt = 1
attempt2 = 1 

while attempt <= 5:
    key_use = input("Enter your Username: ")
    if attempt == 5:
        print("Access denied.\n\n\n")
        exit()
    elif attempt <= 5 and key_use != user: 
        print("Incorrect Username. Try Again.\n")
        attempt += 1
    elif key_use == user:
        print("")
        break

while attempt2 <= 5:
    key_pass = input("Enter your Password: ")
    if key_pass == password:
        print("Access Granted.\n")
        break
    elif attempt2 == 5:
        print("Accessn denied.\n\n\n")
        exit()
    elif attempt2 <= 5 and key_pass != password:
        print("Incorrect Password. Try again.\n")
        attempt2 += 1

print(f"Welcome {user}.")
print("\n\n\n")
print("\n\n\n")

#da computer
user = ("cool")
password = ("cooler") 

def useloop():
    key_use = input("Enter your Username: ")
    if key_use == user:
        print("")
        def passloop():
            key_pass = input("Enter your Password: ")
            if key_pass == password:
                print("Access Granted.\n\n")
            else:
                print("Incorrect Password. Try again.\n")
                passloop()
        passloop()
    else: 
        print("Incorrect Username. Try Again.\n")
        useloop()
useloop() 
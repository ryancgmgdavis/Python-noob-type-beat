
print("\n\nAyy there customer! Welcome to Tony Spandoolie's shoppin' mart!\n")

class Cart:
    items = []
    prices = []
    quantities = []
    totals = []

    def directory(self):
        while True:
            options = input("\nDo one of these:\n1. Add item to cart\n2. Remove item from cart\n3. Veiw cart\n4. Checkout\n")
            if options == "1":
                self.add()
            elif options == "2":
                self.remove()
            elif options == "3":
                self.view()
            elif options == "4":
                self.checkout()

    def add(self):
        item = input("What item would you like to add? ").lower()
        try:
            self.items.index(item)
        except:
            while True:
                try:
                    price = float(input(f"What is the {item}'s price? $"))
                except:
                    print("Price must be an integer.")
                else:
                    while True:
                        try:
                            quant = int(input(f"how many {item}s are you buying? "))
                        except:
                            print("Quantity must be a whole number.")
                        else:
                            self.items.append(item)
                            self.quantities.append(quant)
                            self.prices.append(price)
                            break
                    break
        else:
            yesno = input(f"you already have {item}s in your cart, would you like to add more? ").lower()
            while yesno != ("no" or "yes"):
                if yesno == "no":
                    self.directory()
                elif yesno == "yes":
                    addquant = input(f"how many more {item}s would you like to add? ")
                    while yesno == "yes":
                        if addquant.isnumeric():
                            loc = self.items.index(item)
                            self.quantities[loc] = self.quantities[loc] + int(addquant)
                            self.directory()
                        addquant = input(f"how many more {item}s would you like to add? ")
                yesno = input(f"you already have {item}s in your cart, would you like to add more? ").lower()

    def remove(self):
        remove = input("What item would you like to remove? ").lower()
        try:
            loc = self.items.index(remove)
        except:
            print(f"{remove} is not in your cart.")
            self.directory()
        else:
            item = self.items[loc]
            quant = self.quantities[loc]
            minus = input(f"You have {quant} {item}s in your cart, how many would you like to remove? ")
            while True:
                if minus.isnumeric():
                    loc = self.items.index(item)
                    self.quantities[loc] = self.quantities[loc] - int(minus)
                    new_quant = self.quantities[loc]
                    if new_quant <= 0:
                        self.items.pop(loc)
                        self.quantities.pop(loc)
                        self.prices.pop(loc)
                    self.directory()
                minus = input(f"You have {quant} {item}s in your cart, how many would you like to remove? ")
        
    def view(self):
        for i in range(len(self.items)):
            print(f"{self.quantities[i]} {self.items[i]}s = ${self.prices[i] * self.quantities[i]:.2f}")

    def checkout(self):
        self.view()
        for i in range(len(self.items)):
            x = self.quantities[i] * self.prices[i]
            self.totals.append(x)
        total = sum(self.totals)
        print(f"Total: ${total:.2f}")
        pay = float(input("What is the payment amout? $"))
        change = float(pay - total)
        print(f"Change due: ${change:.2f}")

        print("Goodbye!")
        exit()

Cart().directory()
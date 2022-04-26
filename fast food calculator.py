print("\n\n\n")
#inputs
#cmc: child meal cost
#amc: adult meal cost
cmc = float(input("How much does a child's meal cost? "))
amc = float(input("How much does an adult's meal cost? "))
num_c = int(input("how many children are there? "))
num_a = int(input("how many adults are there? "))
tax = float(input("what is the sales tax rate? "))

#behind the scenes numbahs B)
tax_p = float(tax / 100)
subtotal = float((cmc * num_c) + (amc * num_a))
tax_monie = float(subtotal * tax_p)
total = float(subtotal + tax_monie)

print("\n")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Sales Tax: ${tax_monie:.2f}")
print(f"Total: ${total:.2f}")
print("\n")

pay = float(input("What is the payment amout? "))

change = float(pay - total)

print(f"Change due: ${change:.2f}")
print("\n\n\n")
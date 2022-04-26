

note = input("Enter the number's notation. ").split()
power = len(note)
number = []

for count in range(1, (power + 1)):
    for value in note:
        product = int(value) * 16 ** (count - 1)
    number.append(product)

print(sum(number))


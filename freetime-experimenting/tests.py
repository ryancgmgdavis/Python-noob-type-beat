
items = ["banana", "bed"]
prices = [2.99, 240.78]
quantities = [5, 2]

loc = items.index("bed")
prices[loc] = prices[loc] + 2
print(prices)
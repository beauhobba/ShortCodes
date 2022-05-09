from itertools import product

colours = ["Blue", "Red", "Orange", "Purple"]

combinations = product(colours, repeat=3)
print(list(combinations))
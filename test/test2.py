from itertools import cycle


fruit = cycle(["apple", "banana", "carrot"])

while(True):
    print(next(fruit))
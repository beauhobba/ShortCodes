def MulTwo(n):
    while True:
        n *= 2
        yield n
        
        
        
        
mulTwo = MulTwo(1)

value =  next(mulTwo)
print(value)


# for value in mulTwo:
#     print(value)
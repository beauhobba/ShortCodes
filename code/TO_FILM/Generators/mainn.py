class Generator:
    def __init__(self):
        self.nums = [2, 3, 5, 10]
    def start_gen(self):
        return (x**2 for x in self.nums)
    
    
g  = Generator()
gen = g.start_gen()

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))    
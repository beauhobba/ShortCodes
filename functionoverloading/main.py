from functools import singledispatchmethod

class Bottle:
    def __init__(self, type):
        self.type = type  
        
class Can:
    def __init__(self, type):
        self.type = type

class Conveyor:
    def __init__(self):
        self.cans = []
        self.bottles = [] 
    
    @singledispatchmethod
    def handle(self, arg):
        raise NotImplementedError("Item not found")
    @handle.register
    def _(self, arg: Bottle):
        self.bottles.append(arg.type)
    @handle.register
    def _(self, arg: Can):
        self.cans.append(arg.type)  
         
    def __str__(self):
        return "Cans: %s \nBottles: %s"%(self.cans, self.bottles)

conveyor = Conveyor() 
bottle =  Bottle("Water")
can =  Can("Coke")

conveyor.handle(bottle)
conveyor.handle(can)
print(conveyor)
      
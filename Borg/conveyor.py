class Conveyer:
    __shared_state = {} 
    def __init__(self):
        self.__dict__ = self.__shared_state
        self.speed = 0
        self.direction = 0
        self.status = 0
    
    def get_speed(self):
        return "Conveyor is going at: "+str(self.speed)+ "m/s"
    
    def change_speed(self, speed):
        self.speed = speed 
        

programmer1 = Conveyer() 
programmer2  = Conveyer() 

programmer1.change_speed(2)
programmer2.change_speed(5)

print(programmer1.get_speed())
print(programmer2.get_speed())
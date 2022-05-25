class Status():
    def __init__(self, current_status, time):
        self.status = current_status 
        self.time = time
    
    def __str__(self):
        return ("Status is: %s \nTime is: %s" % (self.status, self.time))


item =Status("Working", "12/06/2022") 
print(item)
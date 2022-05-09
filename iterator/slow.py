colours = ["Blue", "Red", "Orange", "Purple"]

# these 2 cannot be scaled 
combinations = [] 
for i in colours:
    for j in colours:
        combinations.append([i, j])
       
            
for i, j in zip(colours, colours):
    combinations.append([i, j])


# This is a bit too complex and hard to read
def product(*args, repeat=2):
    pools = [vars for vars in args] * repeat
    
    result = [[]]
    for pool in pools:
        c_result = []
        for x in result:
            for y in pool:
                c_result.append(x+[y])
        result = c_result
    return result
 

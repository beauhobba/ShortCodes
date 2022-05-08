def oven(arg):
    print("Putting "+str(arg)+" in the oven")
    
def oven_cooking(arg):
    print("Cooking for "+str(arg)+ " minutes")

def oven_list(arg):
    for ing in arg:
        print("Adding "+str(ing)+ " to the oven")
        
oven("pie")
oven_cooking(1)
oven_list(["mince", "carrots"])

from functools import singledispatch

@singledispatch
def oven(arg):
    print("Putting "+str(arg)+" in the oven")
    
@oven.register
def _(arg: int):
    print("Cooking for "+str(arg)+ " minutes")

@oven.register
def _(arg: list):
    for ing in arg:
        print("Adding "+str(ing)+ " to the oven")

oven("pie")
oven(1)
oven(["mince", "carrots"])
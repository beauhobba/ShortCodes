def sub(x, y):
    return x - y

def add(x, y):
    return x + y

def mul(x, y):
    return x *  y

def div(x, y):
    return x / y

operations = {
    'ADD': add,
    'SUB': sub,
    'MUL': mul,
    'DIV': div
        }

print(operations['DIV'](1, 2))

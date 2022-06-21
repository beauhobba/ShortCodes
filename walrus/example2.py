num_list = [1, 22, 35, 12, 14]

def floor_div(num):
    return num // 2

print([floor_div(x) for x in num_list if floor_div(x) > 10])

print([y for x in num_list if (y:=floor_div(x)) > 10])
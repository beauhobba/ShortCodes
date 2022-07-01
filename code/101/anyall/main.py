arr = ["eggs" , "carrots", "beans", "milk"]

def check_all(arr): 
    for item in arr:
        if("e" in item):
            continue
        else:
            return False
    return True  


def check_any(arr): 
    for item in arr:
        if("e" in item):
            return True 
        else:
            continue
    return False   


print(check_all(arr))
print(check_any(arr))

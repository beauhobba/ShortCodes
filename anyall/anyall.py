arr = ["eggs" , "carrots", "beans", "milk"]

all_arr = all("e" in x for x in arr)
any_arr = any("e" in x for x in arr)

print(all_arr)
print(any_arr)
def factorial(k):
    if(k > 1):
        result = k*factorial(k-1)
    else:
        result = 1 if k==0 else k
    return result

print(factorial(6))
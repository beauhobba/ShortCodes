def factorial(k):
    for i in range(1, k):
        k *= i
    return 1 if k==0 else k
        
print(factorial(6))
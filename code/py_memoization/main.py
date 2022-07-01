import functools
import datetime

@functools.cache
def fib(num):
    if num < 2:
        return num
    else:
        return fib(num-1) + fib(num-2)
      
      
if __name__ == "__main__":   
    a = datetime.datetime.now()
    print(fib(36))
    print(fib(36))
    b = datetime.datetime.now()
    print("Total Time Taken: "+str((b-a).total_seconds() * 1000))
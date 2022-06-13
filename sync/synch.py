import time

def call_centre():
    print("Waiting for customer service")
    time.sleep(1)
    return "Call has started"

def eat_lunch():
    print("Starting to eat lunch")
    time.sleep(1)
    return "Lunch has been eaten"


def main():
    start = time.time()
    
    call = call_centre()
    print(call) 
    eat = eat_lunch()
    print(eat)
    
    end = time.time()
    print("Time Taken: %d mins" % (end - start))
    
main() 
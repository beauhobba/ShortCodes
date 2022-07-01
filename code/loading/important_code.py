import time


for i in range(100):
    print("Starting Iteration: "+str(i)+"/100")
    if(i == 3):
        time.sleep(10)
    print("Finished Iteration: "+str(i)+"/100"+" --> Time: 0.001ns")
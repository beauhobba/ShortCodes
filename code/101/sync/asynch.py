import asyncio
import time

async def call_centre():
    print("Waiting for customer service")
    await asyncio.sleep(1)
    return "Call has started"

async def eat_lunch():
    print("Starting to eat lunch")
    await asyncio.sleep(1)
    return "Lunch has been eaten"


async def main():
    start = time.time()
    
    call = asyncio.create_task(call_centre())
    eat = asyncio.create_task(eat_lunch())
    
    call_status = await call 
    eat_status = await eat
    
    print(eat_status)
    print(call_status)
    
    end = time.time()
    print("Time Taken: %d mins" % (end - start))
    
    
asyncio.run(main())
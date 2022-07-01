# Asynch vs Sycnh Programming in Python

Youtube explanation is here: https://youtube.com/shorts/gdF8EUWhfFE

<br>
<br>

## Script
Why wait for unrelated tasks to run after each other

Synchronous vs asyncrhonous coding is something you should always consider when you program. 
In ythis code we have a person who calls a call centre and then eats their lunch.
The call centre has a 1 minute wait time and the person takes 1 minute to eat their lunch. If we press run on this, we see it takes 2 minutes for both tasks to be executed.

This is known as asycnrhornous programming. Where each operation occurs after each other.
What we can instead do is perform aschronous programming. Now each operation can occur at any time.

Back to the code, we add the asyncio library. The functions we use the asynch and await keyword.

To run the code we create asycnrhoous tasks, and we await the results using the awaitkeyword again.
As you can see now we can eat the lunch whilst we wait for the call centre, and the task only takes 1 minute 

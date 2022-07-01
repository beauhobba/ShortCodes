# Walrus in Python

Youtube explanation is here: https://www.youtube.com/watch?v=mEwUnrBaEZQ&ab_channel=BeauHobba

<br>
<br>

## Script:
This is why walruses are in python

Lets say we have a simple null checker, where in this case we check if the variable a is not none and then print it.
it is quite annoying that we need to initalise a, check it and print it in seperate lines

This is where the walrus operator comes in:
This operator lets us assign a value to a variable in an expression.
So now we can initialise a whilst performing the none check and then print it.


This can also help eliminate calling functions for no reason.
Lets say we want to loop through this number list and return a new list of all numbers which when dividied by 2 are greater than 10
Here you can  see we use our function call twice.

We can call it once using the walrus operator, which instead now initialises the y variable and provides the same results at a lesser expesnes. Because

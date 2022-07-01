# Partials in Python

Youtube explanation is here: https://www.youtube.com/shorts/bf1D7gIdLAA?&ab_channel=TheMomentShorts


<br>
<br>

## Script:
This is how you avoid silly errors.

In this code I have a 2 crypto currencies in a dictionary. The function set_amount takes a cryptocurrency and changes
its value. If it dosent have the cryptocurrency in its dictionary it returns an error.

However I suck at typing, and sometimes I want my code to accomodate for very simple functions.

We can avoid this potential error completely, and instead use a partial function. 

Partial functions take a function and then create a new usuable function which has less parameters than the original. 
It helps lock down certain functions to allow for more convenient and ease free coding.

In the code we import partial from functools and create 2 new functions set_bitcoin and set_dogecoin. 
We put the main function as the first argument, and then we preset the crypto value as the next argument.
Now we can use our partial functions and avoid any Keyerrors 

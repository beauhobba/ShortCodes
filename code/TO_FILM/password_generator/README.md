# Password Generation in Python

Youtube explanation is here: https://www.youtube.com/watch?v=QtGtollqwAI&ab_channel=BeauHobba


<br>
<br>

# Script
Here is why your password can be cracked easily.

Entropy is a measure of how unpredictable a password can be. It is a simple equation, where a large entropy means a better password

You already know putting your name and birthdays as a password is just asking for it.
 Instead you can put a large range of random characters. In the code we do this by:
 
putting a large range of ascii characters into a string. Selecting our password strenght.
And then using random to select 10 of these characters.
Now we get a secure password which we can use.

However, it is very hard to remember this password and it isnt even the best option. 
There are a lot of words in the English dictionary and instead of using random characters we can use random words. 
To do this in the code we get a dictionary of random words, make the data usable. We then loop through the data and pick 5 or more random words
and join them togethor. In this case we got: 
As you can see the entropy of this 5 words is higher than the random characters, and this is much easier to understand.

If we want a very secure password, you can either increase the amount of characters or words, or you can replace some characters with capital letters.
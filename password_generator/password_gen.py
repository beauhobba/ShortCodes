import random
import requests

word_site = "https://www.mit.edu/~ecprice/wordlist.10000"

response = requests.get(word_site)
WORDS = response.content.splitlines()

selected_words = [x.decode()+" " for x in random.sample(WORDS, 4)]
password = "".join(selected_words)

# password = password.replace("o", "0")
# password = password.replace("l", "1")
# print(password)

# https://xkcd.com/936/
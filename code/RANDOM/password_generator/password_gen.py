import random
import requests

word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
password_length = 5

response = requests.get(word_site)
WORDS = response.content.splitlines()

selected_words = [x.decode()+" " for x in random.sample(WORDS, password_length)]
password = "".join(selected_words)

print(password)
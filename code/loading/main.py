from tqdm import tqdm
from time import sleep

tests = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

for test in tqdm(tests, colour='GREEN', desc='Tests'):
    sleep(0.25)
    


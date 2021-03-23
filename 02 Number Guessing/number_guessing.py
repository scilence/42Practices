from random import random
from random import randrange

print("Guessing Number: 1 ~ 100\n")

current = randrange(1, 100, 1)
idx = 0

while True:
    idx += 1
    guessNumber = input("please input numbers (" + str(idx) + "): ")
    if(current == int(guessNumber)):
        break

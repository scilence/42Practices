from random import random
from random import randint

print("Guessing Number: 1 ~ 100\n")

current = randint(1, 100)
idx = 0

while True:
    idx += 1
    guessNumber = input("please input numbers (" + str(idx) + "): ")
    if(current == int(guessNumber)):
        break

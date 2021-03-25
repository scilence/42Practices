from random import random
from random import randrange

print("Guessing Number: 1 ~ 100\n")

min = 1
max = 100
answer = randrange(min, max, 1)
guess = 0
idx = 0

while guess != answer:
    idx += 1
    uGuess = input(f"please input numbers ({min} ~ {max}): ")
    if(uGuess == "q"):
        print(f'answer is {answer}')
        break
    guess = int(uGuess)
    if(answer == int(guess)):
        print(f"BINGO!! ANSWER IS '{answer}', You try {idx} times.")
        break
    elif guess < min or guess > max:
        print("Wrong!!, try again")
    else:
        min = guess if answer > guess else min
        max = guess if answer < guess else max

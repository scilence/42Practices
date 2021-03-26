from random import randint


def rollDice():
    num = randint(1, 6)
    print(f"Number is {num}!!")


while(True):
    res = input("ROLL DICE? (y)")
    if res != "y":
        break
    rollDice()

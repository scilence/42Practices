from random import choice
from random import choices
from functools import reduce

quesions = ['monkey', 'apple', 'dice', 'card', 'titanic']
count = 0
answer = ''

ques = choice(quesions)

maskQues = reduce(lambda x, y:  x + y if choices(
    [True, False], weights=[0.3, 0.7]).pop() else x + '_', [char for char in ques])

while answer.lower() != ques.lower():
    answer = input(f"Guess {maskQues}:")
    if answer.lower() == ques.lower():
        print("BINGO!!")

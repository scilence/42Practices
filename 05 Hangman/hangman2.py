from random import choice
from random import choices
from functools import reduce

quesions = ['monkey', 'apple', 'dice', 'card', 'titanic', 'panic', 'travel']
count = 0

ques = choice(quesions)
answer = "".join(['_' for char in ques])

while answer.lower() != ques.lower():
    iChar = input(f"Guess ({answer}):")
    strs = [char if iChar == char else answer[idx]
            for idx, char in enumerate(ques)]
    answer = "".join(strs)

print(f"BINGO!! [{answer}]")

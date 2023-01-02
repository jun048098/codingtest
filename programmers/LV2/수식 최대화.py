from itertools import permutations
from collections import deque

def calculation(e, o):
    q= deque()
    for now in e:
        s = ''
        if now.isdigit() == True:
            s += now
        else:


    return

def solution(expression):
    for oper in permutations(('+', '-', '*'), 3):
        calculation(expression, oper)
    answer = 0
    return answer
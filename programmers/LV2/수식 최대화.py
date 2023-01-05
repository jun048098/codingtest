from itertools import permutations
from collections import deque

def operate(f, s, o):
    if o == '+':
        return f + s
    elif o =='*':
        return f * s
    elif o == '-':
        return f - s

def calculation(e, o):
    q= deque()
    s = ''
    for now in e:
        if now.isdigit() == True:
            s += now
        else:
            q.append(int(s))
            q.append(now)
            s=''
    q.append(int(s))

    for p in o:
        stack = deque()
        while q:
            tmp = q.popleft()
            if tmp == p:
                f, s = stack.pop(), q.popleft()
                stack.append(operate(f,s, p))
            else:
                stack.append(tmp)
        q = stack
    return abs(q[0])

def solution(expression):
    answer = 0
    for oper in permutations(('+', '-', '*'), 3):

        answer = max(calculation(expression, oper), answer)
        print(answer)

    return answer
print(solution("100-200*300-500+20"))
'''
[100- {(200*300)-500}] +20

'''

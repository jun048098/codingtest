from collections import deque

def check(w):
    q = deque()
    for i in w:
        # 소괄호
        if i == '(':
            q.append('(')
        elif i == ')':
            if len(q) >= 1:
                if q[-1] == '(':
                    q.pop()
            else:
                return 0
        # 중괄호
        if i == '{':
            q.append('{')
        elif i == '}':
            if len(q) >= 1:
                if q[-1] == '{':
                    q.pop()
            else:
                return 0
        # 대괄호
        if i == '[':
            q.append('[')
        elif i == ']':
            if len(q) >= 1:
                if q[-1] == '[':
                    q.pop()
            else:
                return 0
    if len(q) == 0:
        return 1
    else:
        return 0

def solution(s):
    answer = 0
    if s ==1:
        return 0

    else:
        for i in range(len(s)):
            answer += check(s)
            s = s[1:] + s[0]

        return answer

a = "[](){}"
b = "}]()[{"
c = "[)(]"
d = "}}}"
e = "[{]}"
print(solution(a))
print(solution(b))
print(solution(c))
print(solution(d))
print(solution(e))
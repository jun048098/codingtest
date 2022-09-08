def solution(s):
    s = list(s + ' ')
    new = [' ']
    for i in range(len(s)):
        if new[-1] == s[i]:
            new.pop()
        else:
            new.append(s[i])

    if len(new) == 0:
        return 1
    else:
        return 0
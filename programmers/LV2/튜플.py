def solution(s):
    s = s.replace('{', '')
    s = s[:-2]
    s = s.split('},')
    s.sort(key=len)
    t = [int(s[0])]

    for i in range(1, len(s)):
        now = set(map(int, s[i].split(',')))
        c = list(now - set(t))
        t.append(c[-1])
    return t


s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
print(solution(s))



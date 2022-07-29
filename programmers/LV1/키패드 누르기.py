def solution(s):
    new_s = s[::-1]
    if new_s == s:
        return 1
    else:
        return -1
s='a'
print(solution(s))
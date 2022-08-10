def solution(n):
    s = ''
    while n >= 1:
        n, d = divmod(n,3)
        s += str(d)
    return int(s,3)
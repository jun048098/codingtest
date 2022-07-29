def solution(n):
    th = ''
    while n>0:
        n, m = divmod(n,3)
        th += str(m)

    return int(th,3)

print(solution(45))
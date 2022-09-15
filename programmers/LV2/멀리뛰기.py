def solution(n):
    a1 = 0
    a2 = 1
    for i in range(1,n+1):
        a2 ,a1 = a1+a2, a2
    return a2%1234567

print(solution(1))
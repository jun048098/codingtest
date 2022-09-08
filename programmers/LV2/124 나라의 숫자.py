def solution(n):
    a = ['1','2','4']
    answer =''
    while n>0:
        n-=1
        n,m = divmod(n,3)
        answer =a[m] +answer
    return answer

print(solution(3))
def change(num, n):
    if num == 0:
        return '0'
    a= ''
    b= '0123456789ABCDEF'
    while num>0:
        num, mod = divmod(num, n)
        a += b[mod]
    return a[::-1]

def solution(n, t, m, p):
    a= ''
    for i in range(t*m):
        a += change(i, n)
    return a[p-1:t*m:m]

print(solution(2,4,2,1))

print(solution(16,	16,	2,	1))
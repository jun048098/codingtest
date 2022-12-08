n = int(input())
u = [0]*n
u[0] = 1
# 인덱스
i2= i3 = i5 = 0
# 배수
n2, n3, n5 = 2, 3, 5
for k in range(1,n):
    u[k] = min(n2, n3, n5)
    if u[k] == n2:
        i2 += 1
        n2 = u[i2] * 2

    if u[k] == n3:
        i3 += 1
        n3 = u[i3] * 3

    if u[k] == n5:
        i5 += 1
        n5 = u[i5] * 5

print(u)

'''
10
4
'''
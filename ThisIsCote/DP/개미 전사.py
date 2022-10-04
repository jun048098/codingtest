n = int(input())
k = [0] + list(map(int, input().split()))

d = [0] * (n+1)
d[1] = k[1]
d[2] = max(k[1], k[2])

for i in range(3, n+1):
    d[i] = max(d[i-1], d[i-2] + k[i])

print(d[-1])

'''
4
1 3 1 5
'''
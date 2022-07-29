# n = int(input())
# a = list(map(int, input().split()))
#
# up = [1 for _ in range(n)]
# down = [0 for _ in range(n)]
# bi = [0 for _ in range(n)]
#
# # up
# for i in range(n):
#     for j in range(i):
#         if a[i] > a[j]:
#             up[i] = max(up[i], up[j]+1)
#
# # down
# for i in range(n-1, -1, -1):
#     for j in range(i, n):
#         if a[i] > a[j]:
#             down[i] = max(down[i], down[j]+1)
#
# for i in range(n):
#     bi[i] = up[i] + down[i]
#
# print(max(bi))
#

# 풀이2
n = int(input())
a = list(map(int, input().split()))
b = a[::-1]

up = [1 for _ in range(n)]
down = [1 for _ in range(n)]
dp = [0 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if a[i] > a[j]:
            up[i] = max(up[i], up[j]+1)

        if b[i] > b[j]:
            down[i] = max(down[i], down[j]+1)

for i in range(n):
    dp[i] = up[i] + down[n-1-i] -1

print(max(dp))
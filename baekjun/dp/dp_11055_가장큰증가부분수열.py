n = int(input())
a = list(map(int, input().split()))
dp = [0 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if a[i] > a[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += a[i]

print(max(dp))

# 풀이2
# n = int(input())
# lst = list(map(int, input().split()))
#
# dp = [x for x in lst]
#
# for i in range(n):
#     for j in range(i):
#         if lst[i] > lst[j]:
#             dp[i] = max(dp[i], dp[j] + lst[i])
# print(max(dp))
import sys
input = sys.stdin.readline

n = int(input())
wine = [0] + [int(input()) for _ in range(n)]

dp = [0 for i in range(n+1)]
dp[1] = wine[1]
if n > 1:
    dp[2] = dp[1] + wine[2]

for i in range(3, n+1):
    dp[i] = max(dp[i-1], wine[i] + dp[i-2], wine[i] + wine[i-1] + dp[i-3])

print(dp[n])
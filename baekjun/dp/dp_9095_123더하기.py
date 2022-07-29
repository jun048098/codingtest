dp = [1 for _ in range(11)]
dp[2] = 2

for i in range(3, 11):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

t = int(input())
for j in range(t):
    n = int(input())
    print(dp[n])
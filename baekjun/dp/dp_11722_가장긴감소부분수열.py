import sys
put = sys.stdin.readline

n = int(put())
a = list(map(int, put().split()))
dp = [1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if a[i] < a[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
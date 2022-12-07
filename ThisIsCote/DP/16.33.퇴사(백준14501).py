n = int(input())
t = [0]
p = [0]
dp = [0] * (n+2)
max_num = 0
for i in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)

for i in range(n,-1,-1):
    time = i + t[i]-1
    if time <= n:
        dp[i] = max(p[i]+dp[time+1], max_num)
        max_num = dp[i]

    else:
        dp[i] = max_num

print(max_num)
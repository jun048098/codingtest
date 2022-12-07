n = int(input())
p =  list(map(int, input().split()))
dp = [1]*(n)
for i in range(1, n):
    for j in range(i):
        # 앞보다 뒤가 작으면
        if p[j]>p[i]:
            dp[i]= max(dp[i], dp[j]+1)
print(n-max(dp))

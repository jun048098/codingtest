def solution(land):
    l = len(land)
    dp = [[0,0,0,0] for _ in range(l)]
    for i in range(4):
        dp[0][i] = land[0][i]
    for i in range(1, l):
        for j in range(4):
            dp[i][j] = land[i][j] + max(dp[i-1][:j]+dp[i-1][j+1:] )

    return max(dp[-1])
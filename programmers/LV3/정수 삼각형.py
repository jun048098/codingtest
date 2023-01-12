def solution(triangle):
    dp = [[0] * (i+1) for i in range(len(triangle))]
    dp[0] = triangle[0]

    for i in range(1, len(triangle)):
        for j in range(i+1):
            if j == 0:
                dp[i][j] = dp[i - 1][0] + triangle[i][j]
            elif j == i:
                dp[i][j] = dp[i - 1][-1] + triangle[i][j]
            else:
                dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]
    return max(dp[-1]), dp


s= [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(s))
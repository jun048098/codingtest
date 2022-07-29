# import sys
# t = int(sys.stdin.readline())
# for i in range(t):
#     n = int(sys.stdin.readline())
#     dp = [[0]*n for _ in range(2)]
#     st = []
#     for j in range(2):
#         st.append(list(map(int, sys.stdin.readline().split())))
#

import sys
t = int(sys.stdin.readline())

for i in range(t):
    n = int(sys.stdin.readline())
    dp = [list(map(int, sys.stdin.readline().split())) for _ in range(2)]

    if n == 1:
        print(max(dp[0][0], dp[1][0]))

    else:
        dp[0][1] += dp[1][0]
        dp[1][1] += dp[0][0]

        for j in range(2, n):
            dp[0][j] += max(dp[1][j-1], dp[1][j-2])
            dp[1][j] += max(dp[0][j-1], dp[0][j-2])
        print(max(dp[0][n-1], dp[1][n-1]))




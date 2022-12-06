def solution(n,m,g):
    for j in range(1,m):
        for i in range(n):
            if i ==0:
                g[i][j] = max(g[i][j-1], g[i+1][j-1]) + g[i][j]
            elif i == n-1:
                g[i][j] = max(g[i][j-1], g[i-1][j-1]) + g[i][j]
            else:
                g[i][j] = max(g[i][j-1], g[i - 1][j - 1],g[i+1][j-1]) + g[i][j]
    answer = -1
    for i in range(n):
        answer = max(g[i][-1], answer)
    return answer

t = int(input())
for i in range(t):
    n,m = map(int, input().split())
    graph = list(map(int, input().split()))
    g= []
    for i in range(0, n*m, m):
        g.append(graph[i:i+m])
    print((solution(n,m,g)))
'''
2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2

3x4 nxm
[1 3 3 2]
[2 1 4 1] 
[0 6 4 7]

'''





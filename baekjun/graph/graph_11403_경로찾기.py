# bfs
# from collections import deque
# n = int(input())
# graph = [list(map(int, input().split())) for _ in range(n)]
# visit = [[0] * n for _ in range(n)]
#
# def bfs(start):
#     q = deque()
#     q.append(start)
#     check = [0 for _ in range(n)]
#
#     while q:
#         now = q.popleft()
#         for i in range(n):
#             if check[i] == 0 and graph[now][i] == 1:
#                 q.append(i)
#                 check[i] = 1
#                 visit[start][i] = 1
#
# for i in range(n):
#     bfs(i)
# for i in visit:
#     print(*i)

# dfs
# n = int(input())
# graph = [list(map(int, input().split())) for _ in range(n)]
# visit = [0 for _ in range(n)]
#
# def dfs(start):
#     for i in range(n):
#         if graph[start][i] == 1 and visit[i] == 0:
#             visit[i] = 1
#             dfs(i)
#
# for i in range(n):
#     dfs(i)
#     print(*visit)
#     visit = [0 for i in range(n)]


# 플로이드 워셜
n =  int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        for k in range(n):
            if graph[j][i] and graph[i][k]:
                graph[j][k] = 1

for i in graph:
    print(*i)
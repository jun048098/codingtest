# dfs
import sys
input = sys.stdin.readline
n = int(input())
start, target = map(int,input().split())
e = int(input())

graph = [[]for _ in range(n+1)]
for i in range(e):
    f , s = map(int, input().split())
    graph[f].append(s)
    graph[s].append(f)

visit = [-1] * (n+1)
visit[start] = 0

def dfs(start):
    for i in graph[start]:
        if visit[i] == -1:
            visit[i]= visit[start] + 1
            dfs(i)
dfs(start)
print(visit[target])





computer = int(input())
num = int(input())
graph = [[]* computer for _ in range(computer+1)]
for i in range(num):
    a,b= map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt =0
visit = [0 for _ in range(computer+1)]
def dfs(v):
    global cnt
    visit[v]=1
    for i in graph[v]:
        if visit[i] == 0:
            dfs(i)
            cnt +=1
dfs(1)
print(cnt, visit)

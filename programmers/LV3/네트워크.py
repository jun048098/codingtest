from collections import deque

def bfs(n, visited, computers, node):
    visited[node] = True
    q = deque()
    q.append(node)
    while q:
        x = q.popleft()
        visited[x] = True
        for y in range(n):
            if computers[x][y] == 1 and visited[y] == False:
                q.append(y)

def solution(n, computers):
    answer = 0
    visited = [False] * n
    for i in range(n):
        if visited[i] == False:
            answer += 1
            bfs(n, visited,computers ,i)

    return answer



n,c = 3,	[[1, 1, 0], [1, 1, 0], [0, 0, 1]]
print(solution(n,c))
from collections import deque

def solution(n, edge):
    inf = float('inf')

    graph = [[] for _ in range(n+1)]
    for x, y in edge:
        graph[x].append(y)
        graph[y].append(x)
    visited = [inf] * (n+1)
    visited[1] = 0
    q= deque()
    q.append((1,0))

    while q:
        now, distance = q.popleft()

        for i in graph[now]:
            if visited[i] == inf:
                q.append((i, distance+1))
            visited[i] = min(visited[i], distance + 1)


    answer = 0
    md = -1
    for i in range(2,n+1):
        if visited[i] == inf:
            continue
        if md < visited[i]:
            answer = 1
            md = visited[i]
        elif md == visited[i]:
            answer += 1

    return answer

n,e = 6,	[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(n,e))
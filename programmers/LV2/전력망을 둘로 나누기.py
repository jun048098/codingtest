from collections import deque

def bfs(start, graph, visit, wire, cnt):
    q = deque()
    q.append(start)
    visit[start] =True
    while q:
        cnt += 1
        node = q.popleft()
        for target in graph[node]:
            if not ((node == wire[0] and target == wire[1]) or (node == wire[1] and target == wire[0])):
                if visit[target] ==False:
                    visit[target] = True
                    q.append(target)
    return cnt

def solution(n, wires):
    answer = float('inf')
    graph=[[] for _ in range(n+1)]
    for w, r in wires:
        graph[w].append(r)
        graph[r].append(w)
    # wires에서 하나씩 끊기
    for w in wires:
        # 탐색
        a = []
        visit = [False] * (n+1)
        for i in range(1, n+1):
            if visit[i] == False:
                cnt = bfs(i, graph, visit, w, 0)
                a.append(cnt)
        answer = min(answer, abs(a[0] - a[1]))
    return answer

n = 9
w=[[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]
print(solution(n,w))


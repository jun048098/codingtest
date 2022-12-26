import heapq

def solution(N, road, K):
    answer = 0
    graph = [[] for _ in range((N+1)) ]
    for a,b,c in road:
        graph[a].append((b,c))
        graph[b].append((a,c))
    distance = [float('inf')]*(N+1)
    distance[1] = 0
    q= []
    heapq.heappush(q, (0, 1))

    while q:
        d, now = heapq.heappop(q)
        if distance[now] < d:
            continue
        for b,c in graph[now]:
            cost = c + d
            if distance[b] > cost:
                distance[b] = cost
                heapq.heappush(q, (cost, b))

    for i in range(1,N+1):
        if distance[i] <= K:
            answer += 1

    return answer

n=5
r = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
k=3
print(solution(n,r,k))
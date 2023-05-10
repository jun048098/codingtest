from collections import deque
def bfs(n,k):
    max_dist = 100001
    dist = [0] * max_dist
    q= deque()
    q.append(n)
    cnt = 0

    while q:
        x = q.popleft()
        if x == k:
            cnt += 1
            continue
        for nx in (x-1, x+1, 2*x):
            if nx >= 0 and nx < max_dist :
                if dist[nx] == 0 or dist[nx] == dist[x] + 1:
                    dist[nx] = dist[x] + 1
                    q.append(nx)

    print(dist[k])
    print(cnt)


n, k = map(int, input().split())
# n,k = 5, 17
bfs(n, k)
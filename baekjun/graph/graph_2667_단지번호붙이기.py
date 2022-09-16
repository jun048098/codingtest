import sys
input = sys.stdin.readline
n = int((input()))
graph = [list(map(int, input().strip())) for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x, y):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False

    if graph[x][y] == 1:
        global cnt
        cnt += 1
        graph[x][y] = 0
        for b in range(4):
            nx = x + dx[b]
            ny = y + dy[b]
            dfs(nx, ny)
        return True
    return False

apart = []
#  단지수, 가구수
apt, cnt = 0, 0
for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            apart.append(cnt)
            apt += 1
            cnt = 0
apart.sort()
print(apt)
for i in apart:
    print(i)

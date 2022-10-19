import sys
from collections import deque
input = sys.stdin.readline
# 보드
n = int(input())
graph = [[0]*(n+1) for i in range(n+1)]
# 사과
k = int(input())
# 사과 위치
for i in range(k):
    a, b = map(int, input().split())
    graph[a][b] +=1

l = int(input())
c = [input().split() for i in range(l)]

def turn(d, next):
    if next == 'D':
        n_d = (d + 1) % 4
    else:
        n_d = (d + 3) % 4
    return n_d


def solution():
    global graph
    global c
    # 방향
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    dirc = 0
    # 현재 시간, 위치
    time = 0
    x, y = 1, 1
    graph[1][1] = 2
    # 이동 경로
    move = deque()
    move.append((x,y))
    # 다음 지시
    command = deque(c)
    n_com = command.popleft()
    # 이동
    for t in range(10000):
        time+=1
        nx = x + dx[dirc]
        ny = y + dy[dirc]
        move.append((nx, ny))
        # 보드 밖이거나 몸일 때
        if nx < 1 or ny < 1 or nx >n or ny>n or graph[nx][ny] ==2:
            return time
        # 사과 아니면 꼬리 삭제
        if graph[nx][ny] == 0:
            tail = move.popleft()
            graph[tail[0]][tail[1]] = 0
        # 전진
        graph[nx][ny] = 2
        # 방향 전환 시간이면
        if time == int(n_com[0]):
            dirc = turn(dirc, n_com[1])
            if command:
                n_com = command.popleft()
        x, y = nx, ny

    return time

print(solution())

'''
6
3
3 4
2 5
5 3
3
3 D
15 L
17 D

10
4
1 2
1 3
1 4
1 5
4
8 D
10 D
11 D
13 L
'''
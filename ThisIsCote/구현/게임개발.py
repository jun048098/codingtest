import sys
input = sys.stdin.readline
n, m = map(int, input().split())
x, y, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]
visit = graph
# 북 서 남 동
next = {0:(0,-1), 3:(-1,0), 2:(0,1), 1:(1,0)}

cnt = 0
answer = 1
while True:
    d = (d + 3) % 4
    nx = x + next[d][0]
    ny = y + next[d][1]

    if visit[nx][ny] == 0:
        visit[nx][ny] = 1
        x = nx
        y = ny
        cnt = 0
        answer +=1
        continue
    else:
        cnt += 1

    if cnt == 4:
        d = (d+2) % 4
        nx = x + next[d][0]
        ny = y + next[d][1]
        if graph[nx][ny] == 0:
            x = nx
            y = ny
            cnt = 0
        else:
            break


print(answer)

'''
현재 1,1
맵 n,m
현재 방향 왼쪽
방문 x면 전진, 방문0면 회전만
4방향 모두 바다, 방문o 뒤로 1칸 뒤쪽이 바다면 멈춤
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1
'''
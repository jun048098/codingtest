def solution(n):
    answer = []
    all = sum(i for i in range(1,n+1))
    tri = [[0]*i for i in range(1,n+1)]
    direction = ((1,0), (0,1), (-1,-1))
    d= 0
    x,y = 0,0
    for i in range(1, all+1):
        tri[x][y] = i
        dx, dy = direction[d]
        nx = x + dx
        ny = y + dy
        if 0 <= nx < n and 0 <= ny < n and tri[nx][ny] == 0:
            x,y = nx, ny
        else:
            d = (d+1) % 3
            dx, dy = direction[d]
            x += dx
            y += dy

    for i in tri:
        answer += i

    return answer


print(solution(6))
'''
1,1
2,1
3,1

0,0
1,0
2,0
3,0
3,1
3,2
3,3
2,2
1,1
2,1
'''
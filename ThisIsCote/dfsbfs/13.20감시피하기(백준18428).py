from itertools import combinations
n = int(input())
graph = []
empty = []
teacher = []
for i in range(n):
    graph.append(input().split())
    for j in range(n):
        if graph[i][j] == 'X':
            empty.append((i,j))
        elif graph[i][j] == 'T':
            teacher.append((i,j))

def check(x,y,d):
    global n
    # 오른쪽
    if d == 0:
        while x < n :
            if graph[x][y]=='S':
                return 'S'
            if graph[x][y] =='O':
                return 'O'
            x += 1
    # 왼쪽
    elif d == 1:
        while x>=0:
            if graph[x][y]=='S':
                return 'S'
            if  graph[x][y] =='O':
                return 'O'
            x -= 1
    # 윗쪽
    elif d == 2:
        while y < n:
            if graph[x][y]=='S':
                return 'S'
            if graph[x][y] =='O':
                return 'O'
            y += 1
    # 아랫쪽
    elif d == 3:
        while y >= 0:
            if graph[x][y]=='S':
                return 'S'
            if graph[x][y] =='O':
                return 'O'
            y -= 1
    return 'O'

# 4방향 확인
def solution():
    for x,y in teacher:
        for i in range(4):
            if check(x,y,i) == 'S':
                return 'S'
    return 'O'

answer = 'NO'
for data in combinations(empty,3):
    for x, y  in data:
        graph[x][y] = 'O'
    if solution() =='O':
        answer ='YES'
        break
    for x, y in data:
        graph[x][y] = 'X'

print(answer)
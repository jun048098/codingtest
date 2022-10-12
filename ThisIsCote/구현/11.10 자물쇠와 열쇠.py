# 카피를 쓸 경우 너무 느림
def rotation_left(key):
    m = len(key)
    new_key = [[] for _ in range(m)]
    for i in range(m):
        for j in range(m):
            new_key[-1-i].append(key[j][i])
    return new_key


def check(n_graph):
    n = len(n_graph)//3
    for i in range(n, 2*n):
        for j in range(n, 2*n):
            if n_graph[i][j] != 1:
                return False
    return True


def solution(key, lock):
    n = len(lock)
    m = len(key)

    # 확인할 큰 틀
    graph = [[0]*(3*n) for _ in range(3*n)]
    # 그래프에 자물쇠 만들기
    for i in range(n):
        for j in range(n):
            graph[n+i][n+j] = lock[i][j]

    # 회전
    for rotate in range(4):
        key = rotation_left(key)
        # 그래프 탐색
        for i in range(2*n):
            for j in range(2*n):
                # 합치기 연산
                for x in range(m):
                    for y in range(m):
                        graph[i+x][j+y] += key[x][y]
                # 확인
                if check(graph) == True:
                    return True
                # 그래프 되돌리기
                for x in range(m):
                    for y in range(m):
                        graph[i+x][j+y] -= key[x][y]

    return False

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key, lock))





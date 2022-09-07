def solution(m, n, board):
    new_board = list(map(list, zip(*board)))
    for i in new_board:
        i.reverse()
    answer = 0

    while True:
        locate = set()

        for i in range(n - 1):
            for j in range(m - 1):
                if new_board[i][j] == new_board[i + 1][j] == new_board[i][j + 1] == new_board[i + 1][j + 1] and \
                        new_board[i][j] != 0:
                    locate |= set([(i, j), (i, j + 1), (i + 1, j), (i + 1, j + 1)])

        if len(locate) == 0:
            break

        answer += len(locate)
        locate = list(locate)
        locate.sort(reverse=True)
        for x,y in locate:
            new_board[x].pop(y)
            new_board[x].append(0)
    return answer



def solution(m, n, board):
    new_board = list(map(list, zip(*board)))
    answer = 0

    while True:
        locate = set()
        # 탐색
        for i in range(n - 1):
            for j in range(m - 1):
                if new_board[i][j] == new_board[i + 1][j] == new_board[i][j + 1] == new_board[i + 1][j + 1] and \
                        new_board[i][j] != 0:
                    locate |= set([(i, j), (i, j + 1), (i + 1, j), (i + 1, j + 1)])

        if len(locate) == 0:
            break

        answer += len(locate)

        # 제거
        for x, y in locate:
            new_board[x][y] = 0
        # 초기화
        for i, y in enumerate(new_board):
            cnt = [0] * y.count(0)
            new_board[i] = cnt + [j for j in y if j != 0]

    return answer
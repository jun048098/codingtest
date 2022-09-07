# def solution(m, n, board):
#     new_board = [list(i) for i in board]
#     answer = 0
#
#     while True:
#         locate = set()
#         # 탐색
#         for i in range(m - 1):
#             for j in range(n - 1):
#                 if new_board[i][j] == new_board[i + 1][j] == new_board[i][j + 1] == new_board[i + 1][j + 1] and new_board[1][j] != 0:
#                     locate.add((i, j))
#                     locate.add((i + 1, j))
#                     locate.add((i, j + 1))
#                     locate.add((i + 1, j + 1))
#
#         if len(locate) == 0:
#             break
#         # 제거
#         answer += len(locate)
#         locate.sort()
#         for i in locate:
#             new_board[i[0]].pop(i[1])
#             new_board[i[0]].insert(0, 0)
#
#     return answer

# mylist = [[1, 2, 3, 4, 5, 6], [7, 8, 9]]
# # new_list = list(map(list, zip(*mylist)))
# print([i for i in zip(*mylist)])

def solution(m, n, board):
    new_board = list(map(list, zip(*board)))
    # for i in new_board:
    #     i.reverse()
    answer = 0

    while True:
        locate = set()
        # 탐색
        for i in range(n - 1):
            for j in range(m - 1):
                if new_board[i][j] == new_board[i + 1][j] == new_board[i][j + 1] == new_board[i + 1][j + 1] and \
                        new_board[1][j] != 0:
                    locate |= set([(i, j), (i, j + 1), (i + 1, j), (i + 1, j + 1)])

        if len(locate) == 0:
            break

        answer += len(locate)
        locate = list(locate)
        # locate.sort(reverse=True)
        # for x,y in locate:
        #     new_board[x].pop(y)
        #     new_board[x].append(0)

        # 제거
        for x, y in locate:
            new_board[x][y] = '_'
        # 초기화
        for i, y in enumerate(new_board):
            cnt = [0] * y.count('_')
            new_board[i] = cnt + [j for j in y if j != '_']

    return answer

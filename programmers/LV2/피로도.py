# # 순열
# from itertools import permutations
# def solution(k, dungeons):
#     answer = 0
#     for i in permutations(dungeons, len(dungeons)):
#         n=k
#         a=0
#         for need, use in i:
#             if n >= need:
#                 n -= use
#                 a += 1
#         answer = max(answer, a)
#     return answer

n=0
check = []
answer = 0
def dfs(k, cnt, dungeons):
    global answer
    answer = max(answer, cnt)
    for i in range(n):
        if k >= dungeons[i][0] and check[i] == 0:
            check[i] = 1
            dfs(k - dungeons[i][1], cnt +1, dungeons)
            check[i] = 0


def solution(k, dungeons):
    global n, check
    n = len(dungeons)
    check = [0] * n
    dfs(k,0, dungeons)
    return answer

k = 80
d  = [[80,20],[50,40],[30,10]]
print(solution(k, d))
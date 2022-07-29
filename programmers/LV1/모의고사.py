#
# a = [1, 2, 3, 4, 5]
# b = [2, 1, 2, 3, 2, 4, 2, 5]
# c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
# q = [1,3,2,4,2]
# answer= [ ]
# def sol(x):
#     if len(x) >= len(q):
#         x_ans = x[:len(q)]
#     else:
#         x_ans = (x * (len(q) // len(x))) + x[:len(q) % len(x)]
#     score = 0
#     for i in range(len(q)):
#         if x_ans[i] == q[i]:
#             score += 1
#     return score
# #
# # ascore = sol(a)
# # bscore = sol(b)
# # cscore = sol(c)
# rating = [sol(a), sol(a), sol(a)]
#
# for i in range(3):
#     if max(rating) == rating[i]:
#         answer.append(i+1)
#
# print(answer)
# print(rating)

def solution(answers):
    answer = []
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    q = answers

    def sol(x):
        cnt = 0
        for i in range(len(q)):
            if q[i] == x[i % len(x)]:
                cnt += 1
        return cnt

    rating = [sol(a), sol(b), sol(c)]
    for i in range(3):
        if max(rating) == rating[i]:
            answer.append(i+1)

    # def sol(x):
    #     if len(x) >= len(q):
    #         x_ans = x[:len(q)]
    #     else:
    #         x_ans = (x * (len(q) % len(x))) + x[:len(q) // len(x)]
    #     score = 0
    #     for i in range(len(q)):
    #         if x_ans[i] == q[i]:
    #             score += 1
    #     return score

    #     rating = [sol(a), sol(b), sol(c)]

    #     for i in range(3):
    #         if max(rating) == rating[i]:
    #             answer.append(i+1)

    return answer, rating
print(solution([1,3,2,4,2]))

########
def solution(answers):
    score = [0, 0, 0, 0]
    result = []
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for i, j in enumerate(answers):
        if j == a[i % len(a)]:
            score[1] += 1
        if j == b[i % len(b)]:
            score[2] += 1
        if j == c[i % len(c)]:
            score[3] += 1
    for i, j in enumerate(score):
        if j == max(score):
            result.append(i)

    return result
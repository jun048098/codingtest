# def solution(A, B):
#     # answer = [[c +d for c, d in zip(a,b)] for a,b in zip(A,B)]
#     answer = [[list(map(sum, zip(*x)))] for x in zip(A,B)]
#     return answer
# print(solution([[1,2], [2,3]], [[3,4],[5,6]]))



# print(list(map(sum, zip(*([1, 2], [3, 4])))))

    # , ([2, 3], [5, 6])]


def solution(a,b):
    return [[e+f for e,f in zip(c,d)]for c,d in zip(a,b)]

print(solution([[1,2], [2,3]], [[3,4],[5,6]]))
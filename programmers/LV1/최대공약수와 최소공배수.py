# def solution(n, m):
#     answer = []
#     small = min([n, m])
#
#     # 최대공약수
#     div = []
#     for i in range(1, small + 1):
#         if n % i == 0 and m % i == 0:
#             div.append(i)
#     answer.append(max(div))
#
#     # 최소공배수
#     answer.append(n * m / max(div))
#
#     return answer

def solution(n, m):
    for i in range(1, min([n, m])+ 1):
        if n % i == 0 and m % i == 0:
            div = i

    return [div, n * m / div]
print(solution(3,12))

def gcdlcm(a, b):
    c, d = max(a, b), min(a, b)
    t = 1
    while t > 0:
        t = c % d
        c, d = d, t
    answer = [c, int(a*b/c)]

    return answer

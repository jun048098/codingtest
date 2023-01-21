def solution(routes):
    answer = 1
    routes.sort()
    start = routes[0][0]
    out = routes[0][1]
    for i, j  in routes:
        if start <= i <= out:
            start = max(i, start)
            out = min(j, out)
        else:
            answer += 1
            start = i
            out = j
    return answer


def solution2(routes):
    answer = 0
    routes.sort(key = lambda x: x[1])
    out = -30001

    for i, o in routes:
        if i > out:
            answer += 1
            out = o
    return answer

r = [[-20,-15], [-14,-5], [-18,-13], [-5,-3]]
print(solution(r))
print(solution2(r))
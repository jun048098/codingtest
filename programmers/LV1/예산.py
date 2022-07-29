def solution(d, budget):
    answer = 0
    d.sort()
    a = []
    cnt = 0
    for i in d:
        if cnt + i <= budget:
            cnt += i
            a.append(i)

    return answer, a

print(solution([1,3,2,5,4],	9))
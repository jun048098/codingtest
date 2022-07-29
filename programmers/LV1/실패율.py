def solution(N, stages):
    fail = {}
    cnt = len(stages)
    for i in range(1, N + 1):
        if cnt != 0:
            fail[i] = stages.count(i) / cnt
            cnt -= stages.count(i)

        else:
            fail[i] = 0
    num = sorted(fail, key=lambda x: fail[x], reverse=True)

    return num
print(solution(5	,[2, 1, 2, 6, 2, 4, 3, 3]))
def solution(n, s):
    if n > s: return [-1]

    answer = [s//n] * n
    m = s%n
    c = 0
    for i in range(m):
        c -= 1
        answer[c] +=1

    return answer

n, s = 2,9
print(solution(n,s))
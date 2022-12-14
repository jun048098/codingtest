from collections import deque

def solution(numbers, target):
    answer = 0
    q = deque()
    q.append((numbers[0], 0))
    q.append((-1 * numbers[0], 0))
    l = len(numbers)
    while q:
        now, idx = q.popleft()
        idx +=1
        if idx < l:
            q.append((now + numbers[idx], idx))
            q.append((now - numbers[idx], idx))
        else:
            if now == target:
                answer += 1

    return answer
n = [1, 1, 1, 1, 1]
t = 3
print(solution(n,t))
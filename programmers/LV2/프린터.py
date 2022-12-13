from collections import deque
def solution(priorities, location):
    answer = 0
    q= deque([(j,i) for i, j in enumerate(priorities)])
    while len(q):
        now = q.popleft()
        if q and now[0] < max(q)[0]:
            q.append(now)
        else:
            answer +=1
            if now[1] == location:
                break
    return answer


p = [2, 1, 3, 2]
l = 2
print(solution(p, l))

p =[1, 1, 9, 1, 1, 1]
l = 0
print(solution(p, l))

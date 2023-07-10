from collections import deque


a, b = map(int, input().split())
# a, b = 2, 162
# a, b = 4, 42
# a, b = 100, 40021
answer = float('inf')
now = [a, 1]
d = deque()
d.append(now)

while d:
    now = d.popleft()
    if now[0] == b:
        answer = now[1]
        continue

    now[1] += 1
    one = int(str(now[0]) + '1')
    if one <= b:
        d.append([one, now[1]])
    
    double = now[0] * 2
    if double <= b:
        d.append([double, now[1]])
    

if answer == float('inf'):
    answer = -1
print(answer)

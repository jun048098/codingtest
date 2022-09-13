# # 시간초과
# def solution(people, limit):
#     people.sort()
#     cnt = 0
#     while people:
#         if len(people) >1 and people[-1] + people[0] <=limit:
#             people.pop(0)
#         people.pop()
#         cnt+=1
#     return cnt
from collections import deque
def solution(people, limit):
    people.sort()
    people =deque(people)
    cnt = 0
    while people:
        if len(people) >1 and people[-1] + people[0] <=limit:
            people.popleft()
        people.pop()
        cnt+=1
    return cnt
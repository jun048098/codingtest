# def solution(skill, skill_trees):
#     answer = 0
#     skill_kinds = len(skill)
#     skill_num = {j:i for i,j in enumerate(skill) }
#     for k in skill_trees:
#         check = [0] * skill_kinds
#         cnt = 0
#         s = list(k)
#         for j in range(len(s)):
#             if s[j] in skill_num:
#                 check[skill_num[s[j]]] = 1
#                 if skill_num[s[j]] > 0 and check[skill_num[s[j]]-1] == 0:
#                     break
#             cnt+=1
#             if len(s) == cnt:
#                 answer +=1
#     return answer
#
from collections import deque
def solution(skill, skill_trees):
    answer = 0
    for k in skill_trees:
        tree = deque(list(skill))
        for s in k:
            if s in tree and s != tree.popleft() :
                break
        else:
            answer += 1

    return answer

# print(solution("CBD",	["BACDE", "CBADF", "AECB", "BDA"]))

a = "BACDE"
a= list(a)
b=[1,100, 3,4,5,6]
b = [99,9,9,9,9,9,9]
for i in range(5):
    print(i)
    if  i != b.pop(0) and i in b :
        print(b)

print(b)
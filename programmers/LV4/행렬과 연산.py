from collections import deque
def solution(rc, operations):
    r_y = deque([deque([i[0] for i in rc]), deque([i[-1] for i in rc])])
    r_mid = deque([deque(i[1:-1]) for i in rc])
    for oper in operations:
        if oper == "ShiftRow":
            r_mid.appendleft(r_mid.pop())
            r_y[0].appendleft(r_y[0].pop())
            r_y[1].appendleft(r_y[1].pop())

        else:
            r_mid[0].appendleft(r_y[0].popleft())
            r_y[1].appendleft(r_mid[0].pop())
            r_mid[-1].append(r_y[1].pop())
            r_y[0].append(r_mid[-1].popleft())

    for i in range(len(rc)):
        r_mid[i].append(r_y[1][i])
        r_mid[i].appendleft(r_y[0][i])
    answer = [list(i) for i in r_mid]
    return answer
print(solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]], ["Rotate", "ShiftRow"]))
print(solution([[8, 6, 3], [3, 3, 7], [8, 4, 9]], ["Rotate", "ShiftRow", "ShiftRow"]))


# 시간초과

# def solution(rc, operations):
#     # rc = np.array(rc)
#     for oper in operations:
#         if oper == "ShiftRow":
#             rc.insert(0, rc.pop())
#
#         if oper == "Rotate":
#             for j in range(len(rc)-1,0,-1):
#                 rc[j].append(rc[j-1].pop())
#
#             for k in range(len(rc)-1):
#                 rc[k].insert(0, rc[k+1].pop(0))
#
#     return rc
# 시간초과
# def solution(rc, operations):
#     rc = deque([deque(i) for i in rc])
#     for oper in operations:
#         if oper == "ShiftRow":
#             rc.appendleft(rc.pop())
#
#         elif oper == "Rotate":
#             for j in range(len(rc)-1,0,-1):
#                 rc[j].append(rc[j-1].pop())
#
#             for k in range(len(rc)-1):
#                 rc[k].appendleft(rc[k+1].popleft())
#     rc =[list(i) for i in rc]
#     return rc
# def solution(rc, operations):
#     # op 압축
#     rc_x = len(rc[0])
#     rc_y = len(rc)
#     rc = deque([deque(i) for i in rc])
#     n_op = []
#     for i in operations:
#         n_op.append(i)
#         if len(n_op) >rc_y and n_op[rc_y:] == ["ShiftRow"]*rc_y:
#             for _ in range(rc_y):
#                 n_op.pop()
#         elif len(n_op) >rc_x and n_op[rc_x] ==['Rotate'] *((rc_x+rc_y)*2-4):
#             for _ in range((rc_x+rc_y)*2-4):
#                 n_op.pop
#     # 회전
#     for oper in operations:
#         if oper == "ShiftRow":
#             rc.appendleft(rc.pop())
#
#         elif oper == "Rotate":
#             for j in range(len(rc)-1,0,-1):
#                 rc[j].append(rc[j-1].pop())
#
#             for k in range(len(rc)-1):
#                 rc[k].appendleft(rc[k+1].popleft())
#     rc =[list(i) for i in rc]
#     return rc

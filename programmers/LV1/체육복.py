def solution(n, lost, reserve):
    # 중복 제거
    new_reserve = [i for i in reserve if not i in lost]
    new_lost = [i for i in lost if not i in reserve]
    for i in new_reserve:
        down = i-1
        up = i+1
        if down in new_lost:
            new_lost.remove(down)
        elif up in new_lost:
            new_lost.remove(up)
    answer = n- len(new_lost)
    return answer


# def solution(n, lost, reserve):
#     answer = 0
#
#     reserve_del = set(reserve) - set(lost)
#     lost_del = set(lost) - set(reserve)
#
#     for i in reserve_del:
#         if i - 1 in lost_del:
#             lost_del.remove(i - 1)
#
#         elif i + 1 in lost_del:
#             lost_del.remove(i + 1)
#
#     answer = n - len(lost_del)

    return answer
print(solution(5,	[2, 4],	[5,3,1]))




def solution(n, lost, reserve):
    n_lost = list(set(lost) - set(reserve))
    n_res = list(set(reserve) - set(lost))
    for i in n_res:
        if i-1 in n_lost:
            n_lost.remove(i-1)
        elif i+1 in n_lost:
            n_lost.remove(i+1)

    return n - len(n_lost)
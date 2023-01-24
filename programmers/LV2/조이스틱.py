def change(target):
    return min(ord(target) - ord('A'), ord('Z') - ord(target) + 1 )




# # 그리디 실패
# def solution(name):
#     answer = 0
#     idx = set()
#     l = len(name)
#     for i in range(l):
#         c = change(name[i])
#         answer += c
#         if c != 0 and i != 0:
#             idx.add(i)
#     now = 0
#     while idx:
#         m = max(idx)
#         n = min(idx)
#         left_len = (l + now - m) % l
#         right_len = (l + n - now ) % l
#         if left_len <= right_len:
#             now = m
#             idx.remove(m)
#             answer += left_len
#         else:
#             now = n
#             idx.remove(n)
#             answer += right_len
#
#     return answer



n = "BBBBAAAABA"
print(solution(n))

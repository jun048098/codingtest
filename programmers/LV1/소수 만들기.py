# def solution(nums):
#     # 합의 조합
#     nums_list = []
#     for i in range(len(nums)):
#         for j in range(i + 1, len(nums)):
#             for k in range(j + 1, len(nums)):
#                 nums_list.append(nums[i] + nums[j] + nums[k])
#
#
#     # 소수 찾기
#     find_prime = set(range(2, max(nums_list) + 1))
#     for i in range(2, max(nums_list)):
#         if i in find_prime:
#             find_prime -= set(range(2 * i, max(nums_list) + 1, i))
#     prime = []
#     for i in nums_list:
#         if i in find_prime:
#             prime.append(i)
#
#     return len(prime)


def solution(nums):
    from itertools import combinations as cb
    answer = 0
    for a in cb(nums, 3):
        cand = sum(a)
        for j in range(2, cand):
            if cand%j==0:
                break
        else:
            answer += 1
    return answer
print(solution([1,2,3,4]))
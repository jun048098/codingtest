# def solution(nums):
#     half = nums/2
#     if half > len(set(nums)):
#         return len(set(nums))
#     else:
#         return half
def solution(nums):
    return min(len(nums)/2, len(set(nums)))
from collections import Counter
# def solution(want, number, discount):
#     answer = 0
#     lw = len(want)
#     wish ={w : n for w, n in zip(want, number)}
#     d = len(discount)
#     for i in range(len(discount)):
#         d = dict(Counter(discount[i:i+10]))
#         check = 0
#         for k, v in wish.items():
#             if k not in d:
#                 break
#             if d[k] >= v:
#                 check += 1
#         if check == lw:
#             answer += 1
#     return answer

from collections import Counter
def solution(want, number, discount):
    answer = 0
    wish ={w : n for w, n in zip(want, number)}
    for i in range(len(discount)):
        d = dict(Counter(discount[i:i+10]))
        if wish == d:
            answer += 1
    return answer
w = ["banana", "apple", "rice", "pork", "pot"]
n = [3, 2, 2, 2, 1]
d = ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]
print((solution(w,n,d)))

w = ["apple"]
n = [1]
d = ["banana", "banana", "banana",  "banana", "banana", "banana", "banana", "banana", "banana", "banana" ] * 10
d.append("apple")
print((solution(w,n,d)))
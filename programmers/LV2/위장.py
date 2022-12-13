# def solution(clothes):
#     h = {}
#     for c in clothes:
#         h[c[1]] = []
#     for c, i in clothes:
#         h[i].append(c)
#     a = 1
#     for i in h.values():
#         a*= len(i)+1
#     return a-1

def solution(clothes):
    h = {}
    for c, k in clothes:
        if k not in h:
            h[k] = 2
        else:
            h[k] += 1
    answer = 1
    for i in h.values():
        answer *= i
    return answer -1
c=[["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(c))
d = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
print(solution(d))
from itertools import product as p
def solution(word):
    answer = []
    for i in range(1,6):
        for c in p(['A','E','I','O','U'], repeat=i):
            answer.append(''.join(c))
    answer.sort()
    return answer.index(word)+1

# print(solution("AAAAE"))
from itertools import permutations


def prime_number(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return 0
    return 1


def solution(numbers):
    answer = 0
    num = list(numbers)
    k = set()
    for i in range(1,len(numbers)+1):
        for j in permutations(num, i):
            k.add(int(''.join(j)))
    for i in k:
        if i < 2:
            continue
        if prime_number(i) == 1:
            answer +=1
    return answer

num="011"
print(solution(num))
from itertools import permutations

def check(ban, per):
    for b, p in zip(ban, per):
        if len(b) != len(p):
            return False

        for i in range(len(b)):
            if b[i] == '*':
                continue
            elif b[i] != p[i]:
                return False
    return True

def solution(user_id, banned_id):
    answer = []
    for per in permutations(user_id, len(banned_id)):
        if check(banned_id, per):
            per = set(per)
            if per not in answer:
                answer.append(per)

    return len(answer)


u = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
b = ["fr*d*", "*rodo", "******", "******"]
print(solution(u,b))
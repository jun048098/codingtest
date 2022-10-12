def solution(s):
    answer = len(s)
    for step in range(1, len(s)//2+1):
        com = ''
        prev = s[0:step]
        count = 1
        for j in range(step, len(s), step):
            print(prev)
            if prev == s[j: j+step]:
                count += 1
            else:
                if count >=2:
                    com += str(count) + prev
                else:
                    com += prev
                prev = s[j: j+step]
                count = 1
        print(com)
        print('  ' + prev)
        # com += str(count) + prev if count >=2 else prev
        answer = min(answer, len(com))
    return answer

s = 'aabbaccc'
print(solution(s))

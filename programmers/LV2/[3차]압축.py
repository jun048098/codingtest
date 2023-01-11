def solution(msg):
    word = {}
    answer = []
    for i in range(26):
        word[chr(ord('A') + i)] = i+1
    if len(msg) == 1:
        return [word[msg]]

    now = 0
    while now <= len(msg):
        cnt = 1
        while cnt < len(msg) and msg[now: now + cnt] in word:
            cnt += 1
        if cnt < len(msg):
            word[msg[now: now + cnt]] = len(word) + 1
        answer.append(word[msg[now: now + cnt-1]])
        now += cnt -1

    return answer

msg = 'A'
print(solution(msg))
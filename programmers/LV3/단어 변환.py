from collections import deque
def solution(begin, target, words):
    if target not in words: return 0
    l = len(words)
    visited = [0] * l
    q = deque()
    q.append((begin, 0))
    while q:
        w, cnt = q.popleft()
        if w == target:
            return cnt
        for i in range(l):
            dif = 0
            if visited[i] == 0:
                for j in range(len(w)):
                    if w[j] != words[i][j]:
                        dif +=1
                if dif == 1:
                    q.append((words[i], cnt + 1))
                    visited[i] = 1

    return cnt

b,t,w = "hit",	"cog",	["hot", "dot", "dog", "lot", "log", "cog"]

print(solution(b,t,w))
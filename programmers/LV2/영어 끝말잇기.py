# def solution(n, words):
#     late = [words[0]]
#     for i in range(1,len(words)):
#         if late[-1][-1] != words[i][0] or words[i] in late:
#             return [i%n+1, (i+n) //n]
#         else:
#             late.append(words[i])
#     return [0,0]

def solution(n, words):
    for i in range(1,len(words)):
        if words[i-1][-1] != words[i][0] or words[i] in words[:i]:
            return [i%n+1, (i+n) //n]
    else:
        return [0,0]
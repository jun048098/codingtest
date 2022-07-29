import re
def solution(dartResult):
    multi = {'S': 1, 'D': 2, 'T': 3}
    opt = {'': 1, '*': 2, '#': -1}
    p = re.compile('(\d+)([SDT])([*#]?)')
    result = p.findall(dartResult)
    answer = []

    for i in range(len(result)):
        if i > 0 and result[i][2] == '*':
            answer[-1] *= 2
        answer.append(int(result[i][0]) ** multi[result[i][1]] * opt[result[i][2]])
    return sum(answer)


print(solution('1S2D*3T'))

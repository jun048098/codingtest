def solution(elements):
    answer = set()
    new_e = elements + elements
    l = len(elements)
    for i in range(1,l+1):
        for j in range(l):
            answer.add(sum(new_e[j:j+i]))
    return len(answer)

e = [7,9,1,1,4]
print(solution(e))
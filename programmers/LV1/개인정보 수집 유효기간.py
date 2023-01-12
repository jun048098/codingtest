def solution(today, terms, privacies):
    answer = []
    t = {}
    for i in terms:
        a, b = i.split()
        t[a] = int(b)

    y, m, d = today.split('.')
    now = int(y)*12*28 + int(m)*28 + int(d)

    for i in range(len(privacies)):
        start, type = privacies[i].split()
        y, m, d = start.split('.')
        end = int(y)*12*28 + int(m)*28 + int(d) + t[type]*28
        if now >= end:
            answer. append(i+1)
    return answer

today="2022.05.19"
terms=["A 6", "B 12", "C 3"]
privacies=["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
print(solution(today,terms, privacies))
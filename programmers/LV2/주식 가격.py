def solution(prices):
    answer = []
    l = len(prices)
    for i in range(l):
        for j in range(i, l):
            if prices[i] > prices[j] or l-1 == j:
                answer.append(j-i)
                break
    return answer
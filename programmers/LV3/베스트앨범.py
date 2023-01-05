def solution(genres, plays):
    songs = {}
    rank = {}
    answer = []
    for i, j in enumerate(zip(genres, plays)):
        g, p =j
        if g in songs:
            songs[g].append([p,i])
        else:
            songs[g] = [[p,i]]

        if g in rank:
            rank[g] += p
        else:
            rank[g] = p

    for granking , playtime in sorted(rank.items(), key = lambda x : x[1],reverse= True):
        for i in sorted(songs[granking], key= lambda x : (-x[0], x[1]))[:2]:
            answer.append(i[1])
    return answer

g=["classic", "pop", "classic", "classic", "pop"]
p=[500, 600, 150, 800, 2500]
print(solution(g,p))
'''
장르별 - 두개씩
많이 재생된 장르
장르에서 많이 재생된 노래
같으면 고유번호 낮은 순
'''


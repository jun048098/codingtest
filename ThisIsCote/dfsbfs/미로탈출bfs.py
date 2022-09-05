def solution(tri):
    new = [[] for _ in range(len(tri))]
    for i in range(len(tri),0,-1):
        # a = [j for j in tri[i] if tri[i].index(j)%2 ==0]
        # index_a = len(tri) - len(a)
        # for i in range(len(a)):
        #     new[i].append(a[i])
        # b = [tri[i][j] for j in range(len(tri[i])) if j%2==1]
        # index_b =len(tri)-len(b)
        # for i in range(len(b)):
        #     new[i].append(b[i])

    # return a #new

tri=[[1], [2,3,4], [5,6,7,8,9]]
print(solution(tri))
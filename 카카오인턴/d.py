def solution(rc, operations):
    for oper in operations:
        if oper == "ShiftRow":
            rc.insert(0, rc.pop())

        if oper == "Rotate":
            for j in range(len(rc)-1,0,-1):
                rc[j].append(rc[j-1].pop())

            for k in range(len(rc)-1):
                rc[k].insert(0, rc[k+1].pop(0))

    return rc
    # answer = [[]]
    # return answer

# solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]], ["Rotate", "ShiftRow"])

# a= [1, 2,3,[4,1]]
# a.insert(0, a.pop())
# solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]], ["ShiftRow"])
#------
# solution= [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for i in range(1, len(solution)):
#     solution.append[i]
#     solution[0].append(solution[1].pop())
# for k in range(len(solution)-1,0,-1):
#     solution[k].insert(0, solution[k-1].pop(0))
# print(solution)



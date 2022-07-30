def solution(id_list, report, k):
    # 리폿수
    report_cnt = {i: 0 for i in id_list}
    # mail = { i :0 for i in id_list}
    report = list(set(report))
    report = [ i.split() for i in report]
    for i in report:
        report_cnt[i[1]] +=1

    # for i in id_list:
    #     if report_cnt[i] >= k:
    #         mail[i] +=1
    answer =[0] * len(id_list)
    for i in report:
        if report_cnt[i[1]] >=k:
            # mail[i[0]] += 1
            answer[id_list.index(i[0])] +=1

    return  answer

print(solution(["muzi", "frodo", "apeach", "neo"]	,["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],	2))
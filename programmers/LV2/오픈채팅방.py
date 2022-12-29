def solution(record):
    user = {}
    answer = []
    for i in record:
        a = i.split()
        if a[0] == 'Enter' or a[0] == 'Change':
            user[a[1]] = a[2]

    for i in record:
        a= i.split()
        if a[0] == 'Enter':
            answer.append("{}님이 들어왔습니다.".format(user[a[1]]))
        elif a[0] == 'Leave':
            answer.append("{}님이 나갔습니다.".format(user[a[1]]))

    return answer



r = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(r))
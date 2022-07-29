def solution(survey, choices):
    point = {"RT" : [0], "TR": [0], "FC": [0], "CF": [0], "MJ": [0], "JM": [0], "AN": [0], "NA": [0]}
    answer = ''
    for i in range(len(survey)):
        if survey[i] == "RT":
            if choices[i] < 4:
                point["RT"].append(4-choices[i])
            elif choices[i] > 4:
                point["TR"].append(choices[i]-4)

        if survey[i] == "TR":
            if choices[i] < 4:
                point["TR"].append(4 - choices[i])
            elif choices[i] > 4:
                point["RT"].append(choices[i] - 4)

        if survey[i] == "CF":
            if choices[i] < 4:
                point["CF"].append(4 - choices[i])
            elif choices[i] > 4:
                point["FC"].append(choices[i] - 4)

        if survey[i] == "FC":
            if choices[i] < 4:
                point["FC"].append(4 - choices[i])
            elif choices[i] > 4:
                point["CF"].append(choices[i] - 4)

        if survey[i] == "MJ":
            if choices[i] < 4:
                point["MJ"].append(4 - choices[i])
            elif choices[i] > 4:
                point["JM"].append(choices[i] - 4)

        if survey[i] == "AN":
            if choices[i] < 4:
                point["AN"].append(4 - choices[i])
            elif choices[i] > 4:
                point["NA"].append(choices[i] - 4)

        if survey[i] == "NA":
            if choices[i] < 4:
                point["NA"].append(4 - choices[i])
            elif choices[i] > 4:
                point["AN"].append(choices[i] - 4)

    score1 = sum(point["RT"]) - sum(point["TR"])
    score2 = sum(point["CF"]) - sum(point["FC"])
    score3 = sum(point["JM"]) - sum(point["MJ"])
    score4 = sum(point["AN"]) - sum(point["NA"])
    if score1 >=0:
        answer = answer + 'R'
    else:
        answer = answer + 'T'

    if score2 >=0:
        answer = answer + 'C'
    else:
        answer = answer + 'F'

    if score3 >=0:
        answer = answer + 'J'
    else:
        answer = answer + 'M'

    if score4 >=0:
        answer = answer + 'A'
    else:
        answer = answer + 'N'

    return answer


solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5])
solution(["TR", "RT", "TR"], [7, 1, 3])




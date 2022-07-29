participant= ["mislav", "stanko", "mislav", "ana"]
completion=["stanko", "ana", "mislav"]
# answer = [i for i in participant if i not in completion]
# print(answer[0])
answer=[]
for i in range(len(participant)):
    if participant[i] not in completion:
        answer.append(participant[i])

print(answer)
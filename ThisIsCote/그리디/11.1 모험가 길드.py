n = int(input())
fear = list(map(int, input().split()))
fear.sort()
group = 0
member = 0

for i in fear:
    member +=1
    if i <= member:
        group += 1
        member = 0

print(group)

'''
5
2 3 1 2 2
'''
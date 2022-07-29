a=[2,1,3,4,1]
b=[]
for i in range(len(a)):
    # k = a.pop(0)
    for j in range(i+1, len(a)):
        b.append(a[i] + a[j])
b = sorted(list(set(b)))
# b.sort()
print(b)



    # for j in a:
    #     print(i +a[j])

# def solution(N, stages):
#     fail = {}
#     stages_user = len(stages)
#     for i in range(1,N+1):
#         if stages_user != 0 :
#             fail[i] = stages.count(i) / stages_user
#             stages_user -= stages.count(i)
#         else:
#             fail[i] = 0
#     answer = sorted(fail,key= lambda x: fail[x] ,reverse=True )
#     return answer

def oddNumbers(l, r):
    # Write your code here
    for i in range(l,r+1):
        if i%2 == 1:
            print(i)

l =2
r = 9
print(oddNumbers(l, r))
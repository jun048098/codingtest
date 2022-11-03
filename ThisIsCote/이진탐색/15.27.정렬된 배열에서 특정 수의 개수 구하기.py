n, x = map(int, input().split())
num = list(map(int, input().split()))
mid = n//2
cnt = 0
while True:
   if num[mid] > x:
       mid =  mid // 2
   elif num[mid] < x:
       mid = (n + mid) //2
   else:
       cnt+=1

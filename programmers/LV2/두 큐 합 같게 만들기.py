from collections import deque
def solution(queue1, queue2):
    q1,q2 = deque(queue1), deque(queue2)
    sum1, sum2 = sum(q1), sum(q2)
    cnt = 0
    for i in range(3*len(q1)):
        if sum1 > sum2:
            sum1 -= q1[0]
            sum2 += q1[0]
            q2.append(q1.popleft())

        elif sum2 > sum1:
            sum2 -= q2[0]
            sum1 += q2[0]
            q1.append(q2.popleft())

        cnt +=1
    return cnt if sum1 ==sum2 else -1

'''
두 큐 하나 원소 pop
다른 큐 insert
각각 합 같도록
최소횟수
1pop 1insert = cnt1
왼쪽 out 오른쪽 insert
불가능 -1

총원소의 합/2

q1 = [3272] 14
q2 = [4651] 16   10
    1 2 1 2 1 10    17
    10 1 2       3

'''
from collections import deque
def solution(queue1, queue2):
    q1,q2 = deque(queue1), deque(queue2)
    sum1, sum2 = sum(q1), sum(q2)
    cnt = 0
    for _ in range(3*len(q1)):
        if sum1 > sum2:
            sum1 -= q1[0]
            sum2 += q1[0]
            q2.append(q1.popleft())

        elif sum2 > sum1:
            sum2 -= q2[0]
            sum1 += q2[0]
            q1.append(q2.popleft())
        else:
            return cnt

        cnt +=1
    return -1
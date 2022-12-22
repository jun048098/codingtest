from collections import deque
def solution(bridge_length, weight, truck_weights):
    time = 1
    all_truck = len(truck_weights)
    out_truck = 0
    truck_weights = deque(truck_weights)
    on_bridge = deque()
    on_weights = 0
    on_truck = 0

    while out_truck != all_truck:
        time += 1
        if truck_weights:
            truck = truck_weights.popleft()
            if on_weights + truck <= weight:
                on_weights += truck
                on_bridge.append((truck, 1))
                on_truck += 1
            else:
                truck_weights.appendleft(truck)

        for i in range(on_truck):
            tr, ti = on_bridge.popleft()

            if ti == bridge_length:
                out_truck += 1
                on_weights -= tr
                on_truck -= 1
            else:
                on_bridge.append((tr,ti+1))

    return time

b = 2
w=10
t = [7,4,5,6]
print(solution(b,w,t))

b=100
w=100
t=[10]

print(solution(b,w,t))
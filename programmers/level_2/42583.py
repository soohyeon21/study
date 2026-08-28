# 42583
# 다리를 지나는 트럭

# 만약 trucks가 비어있으면, 그냥 bridge.leftpop()과 sec+=1만 해줘도 된다. 굳이 trucks를 0으로 늘릴 필요x.

from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque([0 for _ in range(bridge_length)])
    trucks = deque(truck_weights)
    
    sec = 0
    done = 0
    while (done != sum(truck_weights)):
        if ((sum(bridge)-bridge[0])+trucks[0] <= weight):
            bridge.append(trucks.popleft())
            trucks.append(0)
        else:
            bridge.append(0)
        
        done += bridge.popleft()
        sec += 1
    return sec

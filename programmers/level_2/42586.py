# 42586
# 기능개발

# break와 while-for를 쓰지 않고 풀 수 있는 방법도 있다!

import math

def solution(progresses, speeds):
    plan = []
    while (progresses):
        days = math.ceil((100-progresses[0])/speeds[0])
        for i in range(len(progresses)):
            progresses[i] += days*speeds[i]
            
        distribute = 0
        for j in range(len(progresses)):
            if (progresses[j] >= 100):
                distribute += 1
            else:
                plan.append(distribute)
                progresses = progresses[j:]
                speeds = speeds[j:]
                distribute = 0
                break
        if (distribute != 0):
            plan.append(distribute)
            break
    return plan

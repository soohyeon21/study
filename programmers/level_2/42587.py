# 42587
# 프로세스

# list.pop(0) # O(n)
# list.pop()  # O(1)
# deque.popleft() # O(1)

# any()

# from collections import deque

def solution(priorities, location):
    ppair = []
    for i in range(len(priorities)):
        ppair.append((priorities[i], 'o' if location==i else 'x'))
        
    order = 1
    while (ppair):
        now = ppair.pop(0)
        
        existLower = False
        for num in range(now[0]+1, 10):
            if (num in [x[0] for x in ppair]):
                existLower = True
        
        # 앞선 우선순위 있음
        if (existLower):
            ppair.append(now)
        # 앞선 우선순위 없음x2
        elif (now[1] == 'o'):
            return order
        else:
            order += 1

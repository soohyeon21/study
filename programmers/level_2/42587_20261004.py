# 42587
# 프로세스
# 2026/10/04

# any()

from collections import deque

def solution(priorities, location):
    queue = deque()
    for idx in range(len(priorities)):
        queue.append((idx, priorities[idx]))
    
    order = 0
    while (queue):
        now_idx, now_prior = queue.popleft()
        
        ## sol1) 나머지 우선순위 모두 찾아서 max값 추출 후 비교
        # rest_priorities = [prior for _, prior in queue]
        # if (now_prior < max(rest_priorities + [0])): # rest_priorities가 비어있는 경우도 고려 필요!
        
        ## sol2) any() 사용
        if any(now_prior < prior for _, prior in queue):
            queue.append((now_idx, now_prior))
        else:
            order +=1
            if (now_idx == location):
                break
            
    return order

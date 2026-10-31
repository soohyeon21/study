# 120876
# 겹치는 선분의 길이

from collections import defaultdict

def solution(lines):
    line = defaultdict(int)
    for each in lines:
        for point in range(each[0], each[1]):
            line[point] += 1
    
    cnt = 0
    for k, v in line.items():
        if (v > 1):
            cnt +=1 
    
    return cnt

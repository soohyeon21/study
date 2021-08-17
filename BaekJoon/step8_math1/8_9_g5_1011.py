# 1011

# code 작성 후에는 example 몇 개 넣어보자. 제일 작은 것부터 시작해서 한 20개 정도?
# 내가 생각하지 못했던 경우로 인한 code modification이 필요할 수도 있다.
# for ex) = 인 경우.

# 수학문제 풀 듯이 vs. 반복문 사용
# 역시, 풀이 방법은 다양하다.
# + 알고리즘의 척도는 시간 복잡도를 위주로 판단함.

import math

t = int(input())

for i in range(t):
    x, y = map(int, input().split())
    
    dist = y - x
    n = (-1 + math.sqrt(1 + 4 * dist)) / 2
    floor = math.floor(n)
    ceil = math.ceil(n)
    
    if (floor == ceil):
        floor -= 1
        
    stand = (floor + 1)**2 # stand for standard. 기준.
    
    if (dist <= stand):
        cnt = 2 * floor + 1
    else: # n > stand
        cnt = 2 * (floor + 1)
        
    print(cnt)

# 26265

# 멘티의 이름은 사전 역순이어야 한다.
# string은 sort(key=lambda x:(x[0], -x[1])) 이런식으로 -가 붙으면 TypeError.

# 1) 아래와 같이 멘토 이름 순으로 sort 하고, 멘토 이름 같으면 reverse 하거나
# 2) 멘티 이름 기준으로 먼저 reverse sort 하고, 멘토 이름 기준으로 sort 하는 방법으로 풀 수 있다.

import sys

def printPair(start, end):
    for part in range(end, start-1, -1):
        print(*pair[part])
        

n = int(sys.stdin.readline())

pair = [sys.stdin.readline().split() for _ in range(n)]
pair.sort(key=lambda x:(x[0], x[1]))

start = 0
end = 0
mentor = pair[0][0]
for k in range(1, n):
    if (pair[k][0] == mentor):
        end = k
    elif (pair[k][0] != mentor):
        printPair(start, end)
        mentor = pair[k][0]
        start = k
        end = k
        
printPair(start, end)

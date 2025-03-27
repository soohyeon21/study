# 1639

# "왼쪽 N자리의 합과 오른쪽 N자리의 합이 일치하면 그 티켓은 행운의 티켓이라고 한다."

import sys

s = sys.stdin.readline().rstrip()

possible = [0]
for start in range(len(s)-1):
    for left_n in range(1, (len(s)-start)//2+1):
        left = s[start:start+left_n][::-1]
        right = s[start+left_n:start+left_n*2]
        if (sum(list(map(int, list(left)))) == sum(list(map(int, list(right))))):
            possible.append(len(s[start:start+left_n*2]))

print(max(possible))

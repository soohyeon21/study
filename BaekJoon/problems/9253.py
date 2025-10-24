# 9253

# "편의상 사용자가 출력한 문자열의 길이가 문제의 답과 동일하고"

import sys

a = sys.stdin.readline().rstrip()
b = sys.stdin.readline().rstrip()
same = sys.stdin.readline().rstrip()

a_split = a.split(same)
b_split = b.split(same)
state = True
if (len(a_split)==1 or len(b_split)==1):
    state = False
else:
    for i in range(2):
        if (len(a_split[i]) == 0 or len(b_split[i]) == 0):
            continue
        if (a_split[i][i-1] == b_split[i][i-1]):
            state = False

if (state):
    print("YES")
else:
    print("NO")

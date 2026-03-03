# 15180

# "If the plan does not visit at least 5 different stations, or if it visits a station more than once,"

import sys

s = int(sys.stdin.readline())
order = [i for i in range(s, 9)] + [i for i in range(1, s)]

now = 0
visit = [order[0]]
while (1):
    ipt = sys.stdin.readline().rstrip()
    if (ipt == "#"):
        break

    if (ipt[0] == 'C'):
        now = (now+int(ipt[1]))%8
    elif (ipt[0] == 'A'):
        now = (now+8-int(ipt[1]))%8
    visit.append(order[now])

print(*visit, end=' ')
if ((len(visit) != len(set(visit))) or (len(visit) < 5)):
    print('reject')

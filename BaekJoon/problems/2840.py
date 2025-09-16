# 2840

# "바퀴에 같은 글자는 두 번 이상 등장하지 않는다."

import sys

n, k = map(int, sys.stdin.readline().split())
wheel = ['?' for i in range(n)]

now = 0
state = True
for _ in range(k):
    s, alp = sys.stdin.readline().split()
    now = (now+int(s))%n
    if (wheel[now] == '?'):
        if (alp in wheel):
            state = False
            break
        wheel[now] = alp
    elif (wheel[now] == alp):
        continue
    else:
        state = False
        break

if (state):
    wheel *= 2
    print(wheel[now] + ''.join(wheel[now+1:now+n][::-1]))
else:
    print("!")

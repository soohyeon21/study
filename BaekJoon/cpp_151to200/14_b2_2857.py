# 2857

# 더 간단히 짜는 것도 가능할 것 같긴 하다만...

# range(1, 6)으로 하고 해당 i에 FBI있으면 list에 i 집어넣기

import sys

agent = []
for _ in range(5):
    name = sys.stdin.readline().rstrip()
    agent.append(name)

num = []
for ID in agent:
    if ("FBI" in ID):
        num.append(agent.index(ID)+1)

num.sort()

if (len(num) != 0):
    for number in num:
        print(number, end=" ")
else:
    print("HE GOT AWAY!")

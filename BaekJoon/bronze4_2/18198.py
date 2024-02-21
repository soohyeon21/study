# 18198

# 사실 이미 승패가 판정되었기 때문에, 규칙 상관 없이 그냥 점수가 더 높은 팀 알려주면 된다.
# 아니면 정말 간단하게, 마지막 득점팀을 우승팀이라고 알려줘도 된다. 득점하면서 게임이 끝났을테니까.

import sys

record = sys.stdin.readline().rstrip()

A, B = 0, 0
for i in range(len(record)//2):
    if (record[2*i] == "A"):
        A += int(record[2*i+1])
    else:
        B += int(record[2*i+1])

if (A > B):
    print("A")
else:
    print("B")

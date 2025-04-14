# 11189

import sys

seat = sys.stdin.readline().rstrip()

for caseud in range(3):
    curr = seat[0]
    adjust = 0
    for prefer in seat[1:]:
        # 들어왔을 때 prefer과 다른 경우
        if (curr != prefer):
            adjust += 1
            curr = prefer

        # 나갈때 바꾸기
        cases = ["U", "D", prefer]
        if (curr != cases[caseud]):
            adjust += 1
        curr = cases[caseud]

    print(adjust)

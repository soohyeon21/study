# 20540

# EISNTFJP를 늘여놓고 해당되는 것을 없애면 정반대의 mbti를 알 수 있다.

import sys

mbti = sys.stdin.readline().rstrip()
coup = ["EI", "SN", "TF", "JP"]
ans = ""

for i in range(4):
    if (mbti[i] == coup[i][0]):
        ans +=  coup[i][1]
    else:
        ans += coup[i][0]

print(ans)

# 17296

# 확인 필요 예시
# 4
# 1 0.5 1 0.5
# >>> 2
# 3
# 0 1 0.5
# >>> 1

# press=False를 설정해놓고, 만약 해당 스테이지에서 버튼을 눌렀다면(>0), press=True로 바꿔주는 방법이 좋다.

import sys

n = int(sys.stdin.readline())
button = list(map(float, sys.stdin.readline().split()))

cnt = 0
press = False

b1 = int(button[0]+0.5)
if (b1 > 0):
    cnt += b1
    press = True

for i in range(n-1):
    if (button[i+1]%1 == 0.5):
        if (not press):
            cnt += 1
            press = True
    cnt += int(button[i+1])
    if (int(button[i+1]) > 0):
        press = True

print(cnt)

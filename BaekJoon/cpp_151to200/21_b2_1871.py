# 1871

# 절댓값: absolute number
# 왜 그런진 모르겠다만 abs()가 생각나버렸따..

# input()을 split("-") 하던가.

# '알파벳 부분의 가치 구하기'가 한번에 이해되지 않았다.

import sys

n = int(sys.stdin.readline())
for _ in range(n):
    plate = sys.stdin.readline().rstrip()
    alp = plate[:3]
    cntn = 0
    for i in range(3):
        od = ord(alp[i]) - 65
        cntn += od * 26**(2-i)
    cntn -= int(plate[4:])
    if (abs(cntn) <= 100):
        print("nice")
    else:
        print("not nice")

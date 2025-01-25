# 24196

# 'i = i+ord(encrypt[i])-64'도 정답 처리되는 것을 보니, 범위를 벗어나는 경우는 없나보다.

# 첫번째 문자는 무조건 포함
# 입력에서 ord(첫번째 문자)-64번째 문자가 그 다음 출력 문자
# 출력한 문자가 입력 문자열에서의 마지막 문자이면 종료

import sys

encrypt = sys.stdin.readline().rstrip()

plain = encrypt[0]
i = 0
while (1):
    if (i == len(encrypt)-1):
        break
    i = (i+ord(encrypt[i])-64)%len(encrypt)
    #i = i+ord(encrypt[i])-64
    plain += encrypt[i]

print(plain)

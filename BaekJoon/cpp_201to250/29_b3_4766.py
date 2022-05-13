# 4766

# string fomatting
# print("%10d" %a) # 전체 자리 수 지정
# print("%.2f" %a) # 소숫점 아래 몇째자리까지인지 지정

import sys

cal = []
while (1):
    tem = float(sys.stdin.readline())
    if (tem == 999):
        break
    else:
        cal.append(tem)

for i in range(1, len(cal)):
    print("%.2f" %(cal[i] - cal[i-1]))

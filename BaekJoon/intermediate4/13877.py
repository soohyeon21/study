# 13877

# input이 '012'처럼 앞자리에 0을 포함할 수도 있으므로, 10진수는 단순 num말고 int(num)으로 출력해야 한다.

import sys

t = int(sys.stdin.readline())
for _ in range(t):
    k, num = sys.stdin.readline().split()
    print(k, end=" ")
    
    # 1) 8 or 9가 있는지 확인
##    if (("9" in num) or ("8" in num)):
##        print(0, end=" ")
##    else:
##        print(int(num, 8), end=" ")
    # 2) ValueError로 확인
    try:
        print(int(num, 8), end=" ")
    except ValueError:
        print(0, end=" ")
        
    print(int(num), int(num, 16))

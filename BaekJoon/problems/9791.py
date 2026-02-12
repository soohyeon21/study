# 9791

import sys

while (1):
    ipt = sys.stdin.readline().rstrip()
    if (ipt == '0'):
        break

    result = ''
    
    num, cnt = ipt[0], 1
    for i in range(1, len(ipt)):
        if (ipt[i] != num):
            result += str(cnt)+num
            num = ipt[i]
            cnt = 1
        else:
            cnt += 1
    result += str(cnt)+num

    print(result)

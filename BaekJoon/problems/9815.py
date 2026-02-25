# 9815

import sys

while (1):
    num = list(str(int(sys.stdin.readline())))
    if (num == ['-', '1']):
        break

    print(f"N={''.join(num)}:")

    cnt = 0
    
    if (num == ['0']):
        cnt = 1
    elif (num == [num[0]]*len(num)):
        print('No!!')
        break

    if (int(''.join(num)) == 6174):
        cnt = 1
    
    while ((int(''.join(num)) != 6174) and (int(''.join(num)) != 0)):
        num = sorted(num)
        e1 = int(''.join(num))
        e2 = int(''.join(num[::-1]))
        print(f"{e2}-{e1}={e2-e1}")

        num = list(str(e2-e1))
        cnt += 1
        
    print(f"Ok!! {cnt} times")

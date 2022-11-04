# 5671

# IOError # 해당 파일이 존재하지 않을 경우 발생하는 에러
# EOFError # 파이썬 입력이 끝날때까지 받는 경우. try-except에서 사용.

# try-except 쓰는 방법도 있음.

import sys

while (1):
    ipt = sys.stdin.readline().rstrip()
    if (ipt == ""):
        break
    else:
        n, m = map(int, ipt.split())

    cnt = 0
    for num in range(n, m+1):
        if (len(set(str(num))) == len(str(num))):
            cnt += 1

    print(cnt)

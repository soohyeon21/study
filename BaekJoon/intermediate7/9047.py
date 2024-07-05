# 9047

# 숫자가 4자리 미만일때는 나머지 자리 0으로 채워주기
# or use zfill(4)

# while (1) 대신 while (num != "6174")도 가능

import sys

t = int(sys.stdin.readline())
for _ in range(t):
    num = list(sys.stdin.readline().rstrip())
    cnt = 0
    if ("".join(num) != "6174"):
        while (1):
            least = sorted(num)
            greatest = least[::-1]
            sub = str(int("".join(greatest)) - int("".join(least)))
            cnt += 1
            if (sub == "6174"):
                break
            else:
                num = list(sub.zfill(4))
    print(cnt)

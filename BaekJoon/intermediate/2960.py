#2960

# del list[index]
# list.remove(value)

# boolean&list를 사용하는 방법도 있다.

# 마지막에 end로 break 하는게 의미 있는 거겠지? 답 나온 이후로는 for문 안돌아가도록 해주니까?

import sys

n, k = map(int, sys.stdin.readline().split())
num = [x for x in range(n+1)]
num[1] = 0

cnt = 0
end = False
for i in range(2, n+1):
    if (num[i] != 0):
        for j in range(1, n//i+1):
            if (num[i*j] != 0):
                cnt += 1
            if (cnt == k):
                end = True
                print(num[i*j])
                break
            num[i*j] = 0
    if (end):
        break

# 10425

# 피보나치 수열의 일부(ex 끝 20자리)로도 구분가능하면, 굳이 수의 자리수 전체를 구할 필요가 없다.

import sys

MAX = 100000
fibb = [0 for x in range(MAX+1)]
fibb[1] = 1
for i in range(2, MAX+1):
    fibb[i] = fibb[i-1] + fibb[i-2]

fibb_dict = {v:k for k, v in enumerate(fibb)}

t = int(sys.stdin.readline())
for _ in range(t):
    fn = int(sys.stdin.readline())
    if (fn == 1):
        print(2)
    else:
        print(fibb_dict[fn])

# 22968

# 흑..어쩐지... 등호 때문에 경계값일때 결과값 출력이 안되어서 오답 처리된 거였다.
# 채점 70-80% 진행되다가 오답 처리되면 등호 같은 소소한 부분 확인하자.

# 혹은, fibo 필요없이 vers[i+2] = vers[i]+vers[i+1]+1 도 성립한다.

import sys

t = int(sys.stdin.readline())
fibo = [1, 2, 3, 5, 8, 13, 21]
vers = [1, 2, 4, 7, 12, 20, 33]
for _ in range(t):
    v = int(sys.stdin.readline())
    while (vers[-1] <= v): # 등호!!
        vers.append(fibo[-1]+vers[-1])
        fibo.append(fibo[-1]+fibo[-2])
    for i in range(len(vers)-1):
        if (vers[i] <= v < vers[i+1]):
            print(i+1)
            break

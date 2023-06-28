# 27494

# python3 시간초과, pypy3 정답 # if문 없이 try-except만 사용했을 경우

# python3로 할거면, 2가 2개 이상 있는지, 2 이후에 0이 있는지, 0 이후에 2가 있는지, 2 이후에 3이 있는지 if로 판단하면 가능.
# 아마 n개 숫자 중에서 가능성 없는건 더 자세히 걸러서 시간을 덜 소모하는 듯.

# 시간초과가 뜬다면, 경우를 조금 더 걸러서 계산의 대상을 줄이도록 하자.

import sys

n = int(sys.stdin.readline())

cnt = 0
for num in range(2023, n+1):
    snum = str(num)
    if ((snum.count("2") >= 2) and ("0" in snum) and ("3" in snum)):
        try:
            t1 = snum.index("2")
            t2 = snum[t1+1:].index("0")
            t3 = snum[t1+t2+2:].index("2")
            t4 = snum[t1+t2+t3+3:].index("3")
        except:
            continue
        cnt += 1

print(cnt)

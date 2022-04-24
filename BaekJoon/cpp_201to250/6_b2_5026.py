# 5026

# split()을 입력받을 때 말고 중간에서도 사용할 수 있음.

# 입력받은 문자열 안에 "="가 있느냐는 방식으로 전개할 수도 있음.
# 그래도 시간은 내가 더 빠르지롱~

import sys

n = int(sys.stdin.readline())
for _ in range(n):
    ipt = sys.stdin.readline().rstrip().split("+")
    if (ipt[0] == "P=NP"):
        print("skipped")
    else:
        print(int(ipt[0]) + int(ipt[1]))

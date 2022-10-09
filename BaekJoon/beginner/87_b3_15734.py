# 15734

# 이 풀이는 간단하기는 한데, 이해가 되는 듯 하면서도 안된달까...?

import sys

l, r, a = map(int, sys.stdin.readline().split())

llot = l+a # L이 더 적은 경우
rlot = r+a # R이 더 적은 경우
same = (l+r+a)//2 # L과 R의 수가 같은 경우

print(min(llot, rlot, same) * 2)

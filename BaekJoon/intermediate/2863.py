# 2863

# 좀 더 자동적인 풀이는 없을까?

# dictionary를 사용해보고 싶었지만...ㅎ


import sys

a, b = map(int, sys.stdin.readline().split())
c, d = map(int, sys.stdin.readline().split())

table = [a/c+b/d, c/d+a/b, d/b+c/a, b/a+d/c]
print(table.index(max(table)))

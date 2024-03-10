# 25828

# indiv: 한 명 한 명 모두 검사
# group: 일단 그룹별로 검사해보고, positive group에 대해서 개인별로 검사 추가 진행

import sys

g, p, t = map(int, sys.stdin.readline().split())
indiv = g*p
group = g + p*t

if (indiv < group):
    print(1)
elif (indiv > group):
    print(2)
else:
    print(0)

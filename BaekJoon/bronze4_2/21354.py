# 21354

# 사과와 배의 개수가 주어진다.
# 각각 개당 가격이 7, 13이라 할 때,
# Alex : 사과 매출이 더 큼
# Petra : 배 매출이 더 큼
# lika : 두 매출이 동일

import sys

a, p = map(int, sys.stdin.readline().split())

apple = a*7
pear = p*13

if (apple > pear):
    print("Axel")
elif (apple < pear):
    print("Petra")
else:
    print("lika")

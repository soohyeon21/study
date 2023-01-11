# 1764

# 지난번 틀린 풀이가 7달 전이라는데, 그때에 비해 성장하기는 했나보다.

# from collections import Counter
# Counter() # dictionary의 확장. object의 종류/갯수 정리해서 dictionary 형태로 알려줌.

# 빈 집합을 생성할때는 a = set() 으로 하면 된다. a = {}은 dictionary 만들기임.
# 그냥 list로 만들고 나서 set() 처리해도 됐을 듯..

# set1 & set2 # 교집합
# set1 | set2 # 합집합
# set1 - set2 # 차집합
# set1 ^ set2 # 대칭 차집합

import sys

n, m = map(int, sys.stdin.readline().split())
hear = {sys.stdin.readline().rstrip()}
for _ in range(n-1):
    hear.add(sys.stdin.readline().rstrip())
see = {sys.stdin.readline().rstrip()}
for _ in range(m-1):
    see.add(sys.stdin.readline().rstrip())

only_hear = hear - see
hear_see = hear - only_hear

final = list(hear_see)
final.sort()

print(len(final))
print(*final, sep="\n")

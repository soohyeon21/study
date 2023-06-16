# 25305

# list를 만들면서 바로 sort도 끝내버릴거면 sort() 말고 sorted()를 쓰자.

import sys

n, k = map(int, sys.stdin.readline().split())
score = list(map(int, sys.stdin.readline().split()))
score.sort(reverse=True)

print(score[k-1])

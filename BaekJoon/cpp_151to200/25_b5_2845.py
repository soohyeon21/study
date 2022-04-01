# 2845

# print(*list) # list 요소들을 띄어쓰며 출력
# print("a", "b", sep="*") # a*b # print() 안에 sep 옵션

import sys

l, p = map(int, sys.stdin.readline().split())
paper = list(map(int, sys.stdin.readline().split()))

num = l * p
for i in range(5):
    paper[i] = str(paper[i] - num)

print(' '.join(paper))

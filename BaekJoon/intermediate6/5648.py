# 5648

# n, *elements # 2번째 값부터는 elements라는 이름의 list에 저장

# "1 2 3\n4 5".split() # ['1', '2', '3', '4', '5']

# read(), readlines() 모두 Ctrl+D로 입력 중단 가능
# sys.stdin.read() # 개행문자(\n) 포함 단일 문자열 반환 # 'd\nf\nd\ns\n'
# sys.stdin.readlines() # 개행문자(\n) 포함 list 반환 # ['3\n', '4\n', '5\n', '6\n', '\n']

import sys

n, *elements = sys.stdin.read().split()
for i in range(int(n)):
    elements[i] = int(elements[i][::-1])

elements.sort()
print(*elements, sep="\n")

# 2592

# list 안에 for문을 넣을 수 있다
# max()의 parameter로 key 값도 있다.

import sys

arr = []
for _ in range(10):
    arr.append(int(sys.stdin.readline()))

print(sum(arr) // len(arr))

narr = list(set(arr))
num = []
for i in range(len(narr)):
    num.append(arr.count(narr[i]))
print(narr[num.index(max(num))])


#
# someone's code
#
numbers = [int(input()) for i in range(10)]
print(sum(numbers)//10)
print(max(numbers, key = numbers.count))

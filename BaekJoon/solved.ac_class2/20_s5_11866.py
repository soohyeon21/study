# 11866

# k는 매번 바뀐다.
# while을 써야 'pop index out of range'를 막을 수 있다. (len(circle) <= num)일 때.
# deque: 양쪽 끝에서 삽입과 삭제가 모두 가능한 자료 구조의 한 형태.
# deque or queue를 사용하는 풀이들이 많더라.


import sys

n, k = map(int, sys.stdin.readline().split())
circle = [x for x in range(1, n+1)]
out = []

num = k-1
for i in range(n):
    while (num >= len(circle)):
        num -= len(circle)
    out.append(str(circle.pop(num)))
    num += (k-1)

rst = "<" + ", ".join(out) + ">"
print(rst)

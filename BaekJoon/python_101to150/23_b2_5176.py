# 5176

# 다 입력받은 후 중복되는 요소 없애주고(set()) 전체 참가자 수에서 빼줘도 되겠다.

def cannot_attend(many, number): # many = m, number = want
    cannot = 0
    people = [x for x in range(1, many+1)]
    for num in number:
        if (num in people):
            people.remove(num)
        else:
            cannot += 1
    return cannot

import sys

k = int(sys.stdin.readline())

for _ in range(k):
    p, m = map(int, sys.stdin.readline().split())
    want = []
    for i in range(p):
        want.append(int(sys.stdin.readline()))
    print(cannot_attend(m, want))

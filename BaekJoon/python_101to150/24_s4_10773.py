# 10773

# list의 값을 없애는 방법에는 pop, remove, del, clear가 있다.
# clear() # element 모두 삭제

# remove가 안되는 이유는, 결과값은 같을 지 몰라도,
# 마지막 요소를 없애는 것이 아니라, 같은 값을 같은 앞부분에 위치한 값을 없애기 때문인 것 같다.

import sys

k = int(sys.stdin.readline())

money = []
for _ in range(k):
    current = int(sys.stdin.readline())
    if (current == 0):
        del money[-1]
        #money.remove(money[-1]) # wrong way
    else:
        money.append(current)
print(sum(money))

# 11286

# 기본 Min Heap
# sort() 할 때처럼, heap()도 첫번째 값이 동일하면, 두번째 값으로 자동 정렬한다.

import sys
import heapq

heap = []
n = int(sys.stdin.readline())
for _ in range(n):
    num = int(sys.stdin.readline())
    if (num != 0):
        heapq.heappush(heap, (abs(num), num))
    else:
        if (not heap):
            print(0)
        else:
            print(heapq.heappop(heap)[1])

# 11279

# python heap은 Min Heap이 default이고, (-num, num)으로 tuple을 사용하면 Max Heap처럼 사용가능하다.
# or (-num)을 넣고, pop 할 때 다시 (-) 붙여주는 방법 사용해도 좋고.

import sys
import heapq

n = int(sys.stdin.readline())
heap = []

for _ in range(n):
    num = int(sys.stdin.readline())
    if (num == 0):
        if (not heap):
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (-num, num))

# 31610

import sys

candy = [int(sys.stdin.readline()) for _ in range(3)]
total = candy[0]*candy[1] + candy[2]
print(total)

# 12605

# " ".join(sent[::-1])

import sys

n = int(sys.stdin.readline())
for i in range(1, n+1):
    sent = sys.stdin.readline().split()
    print(f"Case #{i}: ", end="")
    print(*sent[::-1])
##    print(f"Case #{i}: {' '.join(sent[::-1])}")

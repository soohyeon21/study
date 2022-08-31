# 25314

# 아, 그냥 "long "을 (n//4)번 곱해줘도(*) 되겠다.

import sys

n = int(sys.stdin.readline())
answer = ""

for i in range(n//4):
    answer += "long "
answer += "int"

print(answer)

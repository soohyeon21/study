# 1789

# 처음에 이상하게 생각해서 이상하게 짜버렸다.
# 첫번째부터 (n-1)번째까지는 1~(n-1)을 match시켜주고,
# n번째 수는 (s-n)을 부여해 준다. 때에 따라 (s-n) = n 일 수도 있겠다.

import math

s = int(input())

simn = math.floor((-1 + math.sqrt(1 + 8 * s)) / 2)
print(simn)

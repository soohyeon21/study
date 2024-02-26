# 24860

import sys

vk, jk = map(int, sys.stdin.readline().split())
vr, jr = map(int, sys.stdin.readline().split())
vh, dh, jh = map(int, sys.stdin.readline().split())

variants = (vk*jk + vr*jr)*(vh*dh*jh)
print(variants)

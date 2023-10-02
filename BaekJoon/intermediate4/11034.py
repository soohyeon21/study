# 11034

# except EOFError를 하면 왜 런타임 에러(IndexError)가 발생할까?

import sys

while (1):
  try:
    kang = list(map(int, sys.stdin.readline().split()))
    print(max(abs(kang[0]-kang[1])-1, abs(kang[1]-kang[2])-1))

  except:
    break

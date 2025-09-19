# 2597

# ruler = max(max(d1, d2) for d1, d2 in dots + [end])
# ruler = max(ruler-middle, middle)

import sys

ruler = int(sys.stdin.readline())
dots = [list(map(int, sys.stdin.readline().split())) for _ in range(3)]

for i in range(3):
    target = dots[i]
    if (target[0] == target[1]):
        continue
    
    middle = (target[0]+target[1])/2
    end = [middle, abs(ruler-middle)]
    for k in range(3):
        dots[k][0] = abs(middle-dots[k][0])
        dots[k][1] = abs(middle-dots[k][1])
    for d1, d2 in dots+[end]:
        ruler = max(d1, d2)

print(f"{ruler:.01f}")

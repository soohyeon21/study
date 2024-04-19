# 15720

# disc_total은 total에서 discount 금액만큼 제해서 만들 수도 있다.

import sys

b, c, d = map(int, sys.stdin.readline().split())
burgers = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)
sides = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)
beverages = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)

total = sum(burgers)+sum(sides)+sum(beverages)

sets = min(b, c, d)
disc_total = 0
for i in range(sets):
    disc_total += (burgers[i]+sides[i]+beverages[i])*0.9
disc_total += sum(burgers[sets:])+sum(sides[sets:])+sum(beverages[sets:])

print(total)
print(int(disc_total))

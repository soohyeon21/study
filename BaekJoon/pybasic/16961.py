# 16961

import sys

n = int(sys.stdin.readline())
total = [0 for x in range(367)]
diff = ["empty" for x in range(367)]
longest = 0

# 1, 2, 3, 5번
for _ in range(n):
    ipt = sys.stdin.readline().split()
    for day in range(int(ipt[1]), int(ipt[2])+1):
        total[day] += 1
        if (ipt[0] == "T"):
            if (diff[day] == "empty"):
                diff[day] = 1
            else:
                diff[day] += 1
        elif (ipt[0] == "S"):
            if (diff[day] == "empty"):
                diff[day] = -1
            else:
                diff[day] -= 1
    # 5번
    longest = max(longest, int(ipt[2])-int(ipt[1])+1)

# 4번
fightx = []
for i in range(len(diff)):
    if (diff[i] == 0):
        fightx.append(total[i])

print(367 - total.count(0))
print(max(total))
print(diff.count(0))
if (not fightx):
    print(0)
else:
    print(max(fightx))
print(longest)

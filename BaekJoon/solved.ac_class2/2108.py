# 2108

# def amean()에서 return f"{result:.0f}"하면 안됨.
# nlist = [3, 0, 0, -1]에서 amean(nlist)값이 -0이 나오는데, -0으로 출력하면 안된다고 함.

# round(4.5) # 4
# f"{4.5:.0f}" # 4

import sys

def amean(nlist):
    result = sum(nlist)/len(nlist)
    return round(result)

def median(nlist):
    return sorted(nlist)[len(nlist)//2]

def mode(nlist):
    cdict = {}
    for num in nlist:
        cdict[num] = cdict.setdefault(num, 0)
        cdict[num] += 1
        
    count = sorted(list(cdict.items()), key=lambda x:(-x[1], x[0]))
    if (len(count) > 1):
        if (count[0][1] == count[1][1]):
            return count[1][0]
    return count[0][0]

def diff(nlist):
    return max(nlist)-min(nlist)


n = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for _ in range(n)]

print(amean(nums))
print(median(nums))
print(mode(nums))
print(diff(nums))

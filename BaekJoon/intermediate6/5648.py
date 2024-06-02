# 5648

##import sys
##
##elements = []
##first = False
##while (1):
##    try:
##        ipt = sys.stdin.readline().rstrip()
##    except EOFError:
##        break
##
##        ipt = ipt.split()
##        if (not first):
##            n = int(ipt[0])
##            ipt = ipt[1:]
##            first = True
##        for num in ipt:
##            elements.append(int(num[::-1]))
##
##elements.sort()
##print(*elements, sep="\n")


import sys

n, *elements = sys.stdin.read().split()
for i in range(int(n)):
    elements[i] = int(elements[i][::-1])

elements.sort()
print(*elements, sep="\n")

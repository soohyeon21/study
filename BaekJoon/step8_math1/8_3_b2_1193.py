# 1193


# 맞는 답이긴 하지만, 조금 더 간단하게!!!!
##x = int(input())
##th, a, b = 0, 0, 0
##
##if (x == 1):
##    a = 0
##    b = 0
##else:
##    while(x > th):
##        th += 1
##        x -= th
##    if (x == 0):
##        if (th % 2 == 0): # th even
##            a = 1
##            b = th
##        else: # th odd
##            a = th
##            b = 1
##    elif (th % 2 == 0): # th even
##        a = x
##        b = (th + 2) - a
##    else: # th odd
##        b = x
##        a = (th + 2) - b
##print("%d/%d" %(b, a))

x = int(input())
th = 1

while (x > th):
    x -= th
    th += 1

if (th % 2 == 0): # th even
    b = x
    a = (th + 1) - b
else: # th odd
    b = (th + 1) - x
    a = x
    
print("%d/%d" %(b, a))

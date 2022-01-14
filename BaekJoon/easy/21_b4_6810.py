# 6810

import sys

isbn = []
num = "9780921418"
for number in num:
    isbn.append(int(number))

for _ in range(3):
    isbn.append(int(sys.stdin.readline()))

rst = 0
for i in range(13):
    if (i % 2 == 0):
        rst += isbn[i] * 1
    else:
        rst += isbn[i] * 3
        
print("The 1-3-sum is {}" .format(rst))

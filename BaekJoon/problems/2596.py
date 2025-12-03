# 2596

import sys

n = int(sys.stdin.readline())
num = sys.stdin.readline().rstrip()

code = {'000000':'A', '001111':'B', '010011':'C', '011100':'D', '100110':'E', '101001':'F', '110101':'G', '111010':'H'}

rst = ''
for i in range(n):
    obj = num[i*6:i*6+6]
    if (obj in code.keys()): # 0 error
        rst += code[obj]
    else:
        for key in code.keys():
            diff = 0
            right = ''
            for j in range(6):
                if (obj[j] != key[j]):
                    diff += 1
                    right += key[j]
                else:
                    right += obj[j]
            if (diff == 1):
                rst += code[right] # 1 error
        if (len(rst) < i+1): # 2+ error
            rst = i+1
            break

print(rst)

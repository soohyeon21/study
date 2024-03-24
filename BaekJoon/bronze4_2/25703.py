# 25703

import sys

n = int(sys.stdin.readline())

for i in range(1, n+1):
    if (i == 1):
        print("int a;\nint *ptr = &a;")
    elif (i == 2):
        print("int **ptr2 = &ptr;")
    else:
        print(f"int {'*'*i}ptr{i} = &ptr{i-1};")

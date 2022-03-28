# 1032

# i->j 순으로 생성되었지만, list에서 j->i 순으로 사용함.

# 다른 풀이들
# 1. set()을 이용해서 중복을 없애고, len()이 1이면 모든 문자가 동일하다.
# 2. b = list(input()) # 하면 하나의 문자열 속 각 문자가 분리되어 list 안에 들어간다.
# ''.join(list_name) # list_name의 각 element들을 붙여서 문자열로 만들어준다.

import sys

n = int(sys.stdin.readline())
fname = []
for _ in range(n):
    fname.append(sys.stdin.readline().rstrip())

stnd = fname[0]
rst = ""
for i in range(len(stnd)):
    fbool = True
    for j in range(1, n):
        if (stnd[i] != fname[j][i]):
            fbool = False
    if (fbool == True):
        rst += stnd[i]
    elif (fbool == False):
        rst += "?"

print(rst) # 굳이 n=1일때 나눌 필요X

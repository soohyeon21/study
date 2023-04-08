# 3613

# 생각하지 못한 error case가 2개 더 있었다.

# string.capitalize() # 첫글자만 대문자

import sys

varr = sys.stdin.readline().rstrip()

varrupper = False
for v in varr:
    if (v.isupper()):
        varrupper = True
        break

result = ""
if (("_" in varr) and (varrupper)):
    result = "Error!"
elif (varr[0].isupper()): # 첫글자 대문자여도 error.
    result = "Error!"
elif ("_" in varr): # Java->C++
    alist = varr.split("_")
    if ("" in alist): # "__"처럼 underbar 2개 이상이 있는 경우도 error 처리 해줘야됨.
        result = "Error!"
    else:
        result = alist[0]
        for i in range(1, len(alist)):
            result += alist[i][0].upper()+alist[i][1:]
else: # C++->Java
    idx = 0
    clist = []
    for i in range(len(varr)):
        if (varr[i].isupper()):
            clist.append(varr[idx].lower()+varr[idx+1:i])
            idx = i
    clist.append(varr[idx].lower()+varr[idx+1:])

    result = "_".join(clist)

print(result)

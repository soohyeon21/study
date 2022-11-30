# 11273

# dictionary 말고 set도 괜춘.
# set(): set.add(), set.discard(), set.clear()

import sys

def adds(dic, num):
    if (num not in dic):
        dic[num] = 1

def removes(dic, num):
    if (num in dic):
        del(dic[num])

def checks(dic, num):
    if (num in dic):
        print(1)
    else:
        print(0)

def toggles(dic, num):
    if (num in dic):
        del(dic[num])
    else:
        dic[num] = 1

def alls(dic):
    dic.clear()
    for i in range(1, 21):
        dic[i] = 1

def emptys(dic):
    dic.clear()

m = int(sys.stdin.readline())
dic = {}
for _ in range(m):
    inpt = sys.stdin.readline().split()
    order = inpt[0]
    num = 0
    if (len(inpt) == 2):
        num = int(inpt[1])

    if (order == "add"):
        adds(dic, num)
    elif (order == "remove"):
        removes(dic, num)
    elif (order == "check"):
        checks(dic, num)
    elif (order == "toggle"):
        toggles(dic, num)
    elif (order == "all"):
        alls(dic)
    elif (order == "empty"):
        emptys(dic)

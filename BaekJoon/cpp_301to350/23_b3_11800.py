# 11800

# 같은 수일 때도 dictionary/list 사용해서 shorter code 가능하다.

import sys

t = int(sys.stdin.readline())
nick = {1:"Yakk", 2:"Doh", 3:"Seh", 4:"Ghar", 5:"Bang", 6:"Sheesh"}
double = ["", "Habb Yakk", "Dobara", "Dousa", "Dorgy", "Dabash", "Dosh"]

for i in range(1, t+1):
    num = list(map(int, sys.stdin.readline().split()))
    num.sort(reverse=True)
    val = ""
    if (num == [1, 1]):
        val = double[1]
    elif (num == [2, 2]):
        val = double[2]
    elif (num == [3, 3]):
        val = double[3]
    elif (num == [4, 4]):
        val = double[4]
    elif (num == [5, 5]):
        val = double[5]
    elif (num == [6, 6]):
        val = double[6]
    elif (num == [6, 5]):
        val = "Sheesh Beesh"
    else:
        val = nick[num[0]] + " " + nick[num[1]]
    print(f"Case {i}: {val}")

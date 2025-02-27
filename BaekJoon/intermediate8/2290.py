# 2290

# case 1 # " - " # " " + "-"*s + " "
# case 2 # "| |" # "|" + " "*s + "|"
# case 3 # "|  " # "|" + " "*(s+1)
# case 4 # "  |" # " "*(s+1) + "|"
# case 5 # "   " # " "*(s+2)

# " - ", "| |", "|  ", "  |", "   " # 5가지 경우로 나누고
# 각 숫자 별로 5개 조합 순서를 찾는다.

import sys

s, n = sys.stdin.readline().split()
s = int(s)

part = {1:" " + "-"*s + " ", 2:"|" + " "*s + "|", 3:"|" + " "*(s+1), 4:" "*(s+1) + "|", 5:" "*(s+2)}
number = {1:"5"+"4"*s+"5"+"4"*s+"5", 2:"1"+"4"*s+"1"+"3"*s+"1", 3:"1"+"4"*s+"1"+"4"*s+"1",
          4:"5"+"2"*s+"1"+"4"*s+"5", 5:"1"+"3"*s+"1"+"4"*s+"1", 6:"1"+"3"*s+"1"+"2"*s+"1",
          7:"1"+"4"*s+"5"+"4"*s+"5", 8:"1"+"2"*s+"1"+"2"*s+"1", 9:"1"+"2"*s+"1"+"4"*s+"1",
          0:"1"+"2"*s+"5"+"2"*s+"1"}

result = ["" for _ in range(2*s+3)]
for each in n:
    order = number[int(each)]
    for i in range(2*s+3):
        result[i] += part[int(order[i])] + " "

for r in result:
    print(r)

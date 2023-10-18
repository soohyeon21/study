# 16205

# 공통으로 묶을 수 있는 것은 최대한 묶어주자.

import sys

num, var = sys.stdin.readline().split()
word = []

# 단어 분리하기
if ((num == "1") or (num == "3")):
    before = 0
    for i in range(1, len(var)):
        if (var[i].isupper() == True):
            word.append(var[before:i].lower())
            before = i
    word.append(var[before:].lower())
elif (num == "2"):
    word = var.lower().split("_")

# var3
var3 = ""
for w in word:
    var3 += w[0].upper()+w[1:]

# var1
var1 = var3[0].lower()+var3[1:]

# var2
var2 = "_".join(word)

print(var1)
print(var2)
print(var3)

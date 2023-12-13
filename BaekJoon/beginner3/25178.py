# 25178

# 굳이 def로 빼지 않아도 되었을듯.

import sys

def con1(w1, w2):
    line1 = sorted(list(w1))
    line2 = sorted(list(w2))
    if (line1 != line2):
        return False
    return True

def con2(w1, w2):
    if ((w1[0] != w2[0]) or (w1[-1] != w2[-1])):
        return False
    return True

def con3(w1, w2):
    for letter in "aeiou":
        w1 = w1.replace(letter, "")
        w2 = w2.replace(letter, "")

    if (w1 != w2):
        return False
    return True


n = int(sys.stdin.readline())
word1 = sys.stdin.readline().rstrip()
word2 = sys.stdin.readline().rstrip()

if (con1(word1, word2) and con2(word1, word2) and con3(word1, word2)):
    print("YES")
else:
    print("NO")

# 7656

# 예제 말고 주어진 조건을 잘 살필 필요가 있다.

import sys

ipt = sys.stdin.readline().rstrip()

sentences = []
sen = ""
for letter in ipt:
    sen += letter
    if (letter in ".?"):
        sentences.append(sen.strip())
        sen = ""

for one in sentences:
    if ((one[:7] == "What is") and (one[-1] == "?")):
        print(one.replace("What", "Forty-two").replace("?", "."))

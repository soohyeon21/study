# 2703

import sys

t = int(sys.stdin.readline())
for _ in range(t):
    encrypt = sys.stdin.readline().replace("\n", "")
    alpha = sys.stdin.readline().rstrip()
    dic = {" ":" "}
    for i in range(26):
        dic[chr(i+65)] = alpha[i]
        
    answer = ""
    for j in range(len(encrypt)):
        answer += dic[encrypt[j]]

    print(answer)

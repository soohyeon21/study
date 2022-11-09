# 9584

# 변수 덜 쓰고, 코드 조금 덜 복잡하게 하면 더 간단하게 작성 가능.

import sys

plate = sys.stdin.readline().rstrip()
n = int(sys.stdin.readline())
db = []
cnt = 0
fraud = []
for _ in range(n):
    db.append(sys.stdin.readline().rstrip())

for i in range(n):
    decision = True
    for j in range(9):
        now = plate[j]
        if ((now.isdigit()) or (now.isupper())): # if not "*"
            if (now == db[i][j]):
                pass
            else:
                decision = False
    if (decision == True):
        cnt += 1
        fraud.append(db[i])

print(cnt) # len(fraud)
print(*fraud, sep="\n")

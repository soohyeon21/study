# 10501

# "The raggedness will be the sum of the penalty scores for every line except the last one."

import sys

paragraph = sys.stdin.readlines()

n = 0
ms = []
for i in range(len(paragraph)):
    paragraph[i] = paragraph[i].replace("\n", '')
    n = max(n, len(paragraph[i]))
    ms.append(len(paragraph[i]))

rscore = sum((n-m)**2 for m in ms[:-1])

print(rscore)

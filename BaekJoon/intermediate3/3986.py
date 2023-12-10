# 3986

# stack을 사용하는 방법도 있다. 그나마 가장 빠른듯.

#
# sol1) (Python3: 31308KB, 168ms)
# replace만 사용하면 시간 초과.
#
##import sys
##
##n = int(sys.stdin.readline())
##words = [sys.stdin.readline().rstrip() for _ in range(n)]
##cnt = 0
##
##for word in words:
##    if (len(word)%2 != 0):
##        continue
##    elif (word[:len(word)//2] == word[len(word)//2:][::-1]):
##        cnt += 1
##        continue
##    
##    for i in range(len(word)//2):
##        word = word.replace("AA", "").replace("BB", "")
##    if (word == ""):
##        cnt += 1
##
##print(cnt)



#
# sol2) 시간이 더 적게 걸릴 줄 알았는데 아님. (Python3: 31308KB, 260ms)
#
import sys

n = int(sys.stdin.readline())
words = [sys.stdin.readline().rstrip() for _ in range(n)]
cnt = 0

for word in words:
    if (len(word)%2 != 0):
        continue
    else:
        for i in range(len(word)//2):
            word = word.replace("AA", "").replace("BB", "")
            if (word[:len(word)//2] == word[len(word)//2:][::-1]):
                cnt += 1
                break

print(cnt)

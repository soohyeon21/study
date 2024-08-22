# 17502

#
# sol1) 틀림
#
##import sys
##
##n = int(sys.stdin.readline())
##word = sys.stdin.readline().rstrip()
##
##result = ""
###ftime = len(word)//2 if (len(word)%2 == 0) else len(word)//2+1
##for i in range(len(word)//2):
##    if ((word[i] == "?") and (word[len(word)-i-1] == "?")):
##        result += "a"
##    elif (word[i] == "?"):
##        result += word[len(word)-i-1]
##    elif (word[len(word)-i-1] == "?"):
##        result += word[i]
##        
##if (len(word)%2 == 1):
##    tmp = word[len(word)//2] if (word[len(word)//2] != "?") else "a"
##    print(result + tmp + result[::-1])
##else:
##    print(result + result[::-1])



#
# sol2) 맞음
#
import sys

n = int(sys.stdin.readline())
word = sys.stdin.readline().rstrip()
rword = word[::-1]

result = ""
for i in range(len(word)):
    if (word[i] != "?"):
        result += word[i]
    elif (rword[i] != "?"):
        result += rword[i]
    else:
        result += "a"
        
print(result)

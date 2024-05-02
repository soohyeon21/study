# 15122

# input n은 0을 포함하고 있지 않는다고 하였음.
# 그러므로, (input_n+1)에 0이 포함되어 있다면, 해당 0들을 1로 바꿔준 수가 그다음 n이 될 수 있다. (sol2)

#
# sol1) 1씩 계속 더하기
#
##import sys
##
##n = int(sys.stdin.readline())
##while (1):
##    n += 1
##    if ("0" not in str(n)):
##        print(n)
##        break



#
# sol2) 0이 나오면 1로 바꿔주기
# or 그냥 단순히 .replace("0", "1") 해줘도 됨.
#
import sys

n = str(int(sys.stdin.readline())+1)

answer = ""
for i in range(len(n)):
    answer += n[i] if n[i]!="0" else "1"

print(answer)

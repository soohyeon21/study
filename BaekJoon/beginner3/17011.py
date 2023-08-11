# 17011

# 마지막에 한 번 더 cnt와 c를 넣어주기 vs 입력 끝의 줄바꿈을 살려서 cnt와 c 별도로 넣지 않아도 되게 하기

#
# sol1
#
##import sys
##
##n = int(sys.stdin.readline())
##for _ in range(n):
##    line = sys.stdin.readline().rstrip()
##    c = line[0]
##    cnt = 1
##    encode = []
##    for i in range(1, len(line)):
##        if (c == line[i]):
##            cnt += 1
##        else:
##            encode.extend([cnt, c])
##            c = line[i]
##            cnt = 1
##    encode.extend([cnt, c])
##    print(*encode)


#
# sol2
#
import sys

n = int(sys.stdin.readline())
for _ in range(n):
    line = sys.stdin.readline()
    c = line[0]
    cnt = 1
    encode = []
    for i in range(1, len(line)):
        if (c == line[i]):
            cnt += 1
        else:
            encode.extend([cnt, c])
            c = line[i]
            cnt = 1
    #encode.extend([cnt, c])
    print(*encode)

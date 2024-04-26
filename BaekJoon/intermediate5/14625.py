# 14625

# start와 end 시간이 동일할 때 주의
# 11:03~11:09 사이에는 0이 7번 등장한다. # .zfill(2)를 사용할 수도 있음.

#
# sol1) while문 길게 조건 부여
#
##import sys
##
##start = list(map(int, sys.stdin.readline().split()))
##end = list(map(int, sys.stdin.readline().split()))
##n = sys.stdin.readline().rstrip()
##
##cnt = 0
##now = [start[0], start[1]]
##while (now[0]*60+now[1] <= end[0]*60+end[1]):
##    if ((n in f"{now[0]:02}") or (n in f"{now[1]:02}")):
##        cnt += 1
##
##    now[1] += 1
##    now[0] += now[1]//60
##    now[1] %= 60
##
##print(cnt)



#
# sol2) while(1)
#
import sys

start = list(map(int, sys.stdin.readline().split()))
end = list(map(int, sys.stdin.readline().split()))
n = sys.stdin.readline().rstrip()

cnt = 0
now = [start[0], start[1]]
while (1):
    if ((n in f"{now[0]:02}") or (n in f"{now[1]:02}")):
        cnt += 1
        
    if ((now[0] == end[0]) and (now[1] == end[1])):
        break

    now[1] += 1
    now[0] += now[1]//60
    now[1] %= 60

print(cnt)

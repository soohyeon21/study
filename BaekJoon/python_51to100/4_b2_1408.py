# 1408

# oh......

# 출력 형태에 조건이 있는 것는 .fomat이나 %를 활용해보자

# 사실 문제가 잘 이해가 안된다.
# "24시간이 되는 순간에" 범인을 잡는 다는 것이 정확히 무슨 뜻일까?
# 일단은, 잡는 것은 정시에만 가능하다고 이해해서 srt[0]*3600만 sec에 넣었는데,
# srt[1], srt[2]도 고려해줘야 하더라.

import sys

now = list(map(int, sys.stdin.readline().split(":")))
srt = list(map(int, sys.stdin.readline().split(":")))

sec = (srt[0] * 3600 + srt[1]*60 + srt[2]) - (now[0]*3600 + now[1]*60 + now[2])
if (sec < 0):
    sec += 24 * 3600
ans = [0, 0, 0]
ans[2] = sec % 60
ans[1] = (sec // 60) % 60
#ans[1] = (sec % 3600) // 60
ans[0] = (sec // 60) // 60

print("%02d:%02d:%02d" %(ans[0], ans[1], ans[2]))


# wrong1
#
##import sys
##
##now = sys.stdin.readline().rstrip()
##start = sys.stdin.readline().rstrip()
##
##now_h = int(now[0:2])
##now_m = int(now[3:5])
##now_s = int(now[6:])
##
##srt_h = int(start[0:2])
##srt_m = int(start[3:5])
##srt_s = int(start[6:])
##
##ans = [str(60 - now_s), str(59 - now_m), str(srt_h - 1 - now_h)]
####ans_s = str(60 - now_s)
####ans_m = str(59 - now_m)
####ans_h = str(srt_h - 1 - now_h)
##
##for i in range(3):
##    if (len(ans[i]) == 1):
##        ans[i] = "0" + ans[i]
##
##print(ans[2] + ":" + ans[1] + ":" + ans[0])



# wrong2
#
##import sys
##
##now = list(map(int, sys.stdin.readline().split(":")))
##srt = list(map(int, sys.stdin.readline().split(":")))
##
##rst = [0, 0, 0]
##if (now[2] != 0):
##    rst[2] = 60 - now[2]
##    srt[1] = 59
##else:
##    rst[2] = 0
##    srt[1] = 60
##rst[1] = srt[1] - now[1]
##
##for i in range(3):
##    if (len(str(rst[i])) == 1):
##        rst[i] = "0" + str(rst[i])
##    else:
##        rst[i] = str(rst[i])
##print(":".join(rst))



# someone's
#
##h1, m1, s1 = map(int, input().split(':'))
##h2, m2, s2 = map(int, input().split(':'))
##t = h2*3600+m2*60+s2 - (h1*3600+m1*60+s1)
##if t < 0:
##    t += 60*60*24
##h = t//3600 
##m = (t%3600)//60 
##s = t%60
##print("%02d:%02d:%02d" % (h,m,s))

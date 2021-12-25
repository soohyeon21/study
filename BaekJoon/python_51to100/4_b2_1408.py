# 1408

# oh......

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


h1, m1, s1 = map(int, input().split(':'))
h2, m2, s2 = map(int, input().split(':'))
t = h2*3600+m2*60+s2 - (h1*3600+m1*60+s1)
if t < 0:
    t += 60*60*24
h = t//3600 
m = (t%3600)//60 
s = t%60
print("%02d:%02d:%02d" % (h,m,s))

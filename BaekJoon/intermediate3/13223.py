# 13223

# 등호 조건 주의. "이 시간은 1초보다 크거나 같고, 24시간보다 작거나 같다."

# minute 계산은 (%3600//60) 또는 (//60%60)

import sys

now = list(map(int, sys.stdin.readline().split(":")))
salt = list(map(int, sys.stdin.readline().split(":")))

salt_sec = salt[0]*60*60 + salt[1]*60 + salt[2]
now_sec = now[0]*3600 + now[1]*60 + now[2]
if (now_sec >= salt_sec):
    salt_sec += 24*60*60

duration_sec = salt_sec - now_sec
#print(f"{duration_sec//3600:02}:{duration_sec%3600//60:02}:{duration_sec%60:02}")
print(f"{duration_sec//3600:02}:{duration_sec//60%60:02}:{duration_sec%60:02}")

# 5704

# 아 짜증나... 자다가 12시 넘겨서 오늘은 제때 push를 못했다. 쳇. 내 잔디밭...
# 아 그와중에 다른 풀이들보다 시간 짧아서 기분은 또 좋네ㅎㅋ

import sys

while (True):
    ipt = sys.stdin.readline().rstrip()
    if (ipt ==  "*"):
        break

    sett = set(ipt)
    if ((len(sett) == 26 and " " not in sett) or (len(sett) == 27 and " " in sett)):
        print("Y")
    else:
        print("N")

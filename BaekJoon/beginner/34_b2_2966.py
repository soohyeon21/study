# 2966

# %를 이용하면 n 길이 만큼의 답안을 조금 더 쉽게 작성할 수 있다.
# if-elif-else 말고 if-if-if를 사용하면 복잡하게 print 작성할 필요가 없다.

import sys

sang = "ABC"
chang = "BABC"
hyeon = "CCAABB"

n = int(sys.stdin.readline())
answer = sys.stdin.readline().rstrip()

wsang = sang * (n//3 + 1)
wsang = wsang[:n]
wchang = chang * (n//4 + 1)
wchang = wchang[:n]
whyeon = hyeon * (n//6 + 1)
whyeon = whyeon[:n]

cnt_sch = [0, 0, 0]
for i in range(n):
    if (answer[i] == wsang[i]):
        cnt_sch[0] += 1
    if (answer[i] == wchang[i]):
        cnt_sch[1] += 1
    if (answer[i] == whyeon[i]):
        cnt_sch[2] += 1

print(max(cnt_sch))
if (cnt_sch.count(max(cnt_sch)) == 3):
    print("Adrian\nBruno\nGoran")
elif (cnt_sch.count(max(cnt_sch)) == 2):
    if (cnt_sch[0] != max(cnt_sch)):
        print("Bruno\nGoran")
    elif (cnt_sch[1] != max(cnt_sch)):
        print("Adrian\nGoran")
    else:
        print("Adrian\nBruno")
else:
    if (cnt_sch[0] == max(cnt_sch)):
        print("Adrian")
    elif (cnt_sch[1] == max(cnt_sch)):
        print("Bruno")
    else:
        print("Goran")

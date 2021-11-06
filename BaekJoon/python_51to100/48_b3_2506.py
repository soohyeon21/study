# 2506

n = int(input())

score = list(map(int, input().split()))

cnt = 0
whole = 0
for sc in score:
    if (sc == 1):
        cnt += 1
    else:
        cnt = 0
    whole += cnt
##    print(cnt, whole)
print(whole)

# 2935

# 제출하고 보니, 굳이 print문을 중복할 필요는 없겠네.

a = []
rt = None

for _ in range(3):
    a.append(input())

if (a[1] == '*'):
    rt = int(a[0]) * int(a[2])
    print(rt)
else: # '+'
    rt = int(a[0]) + int(a[2])
    print(rt)

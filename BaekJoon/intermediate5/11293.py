# 11293

# >>> *a, b, c = input().split()
# >>> 1 2 3 4 5 ee rr
# a = ['1', '2', '3', '4', '5']
# b = 'ee'
# c = 'rr'

# >>> a1, a2, a3, a4, a5 = map(lambda x: int(x)-1, a)
# a1 = 0, a2 = 1, a3 = 2, a4 = 3, a5 = 4

import sys

c = int(sys.stdin.readline())
for idx in range(1, c+1):
    ans_cnt = int(sys.stdin.readline())
    answers = {dic_idx:sys.stdin.readline().rstrip().replace(" ", "") for dic_idx in range(1, ans_cnt+1)}
    print(f"Customer {idx}")
        
    atp_cnt = int(sys.stdin.readline())
    for i in range(atp_cnt):
        attempt = sys.stdin.readline().split()
        if ((answers[int(attempt[0])][int(attempt[1])-1] == attempt[3]) and (answers[int(attempt[0])][int(attempt[2])-1] == attempt[4])):
            print("correct")
        else:
            print("error")

# 10105

import sys

n = int(sys.stdin.readline())

student = sys.stdin.readline().split()
partner = sys.stdin.readline().split()

sp = {student[i]:partner[i] for i in range(n)}

state = True
cnt = 0
for person in student:
    if ((sp[sp[person]] != person) or (sp[person] == person)):
        state = False
    else:
        cnt += 1
        
if (not state or (cnt != n)):
    print("bad")
else:
    print("good")

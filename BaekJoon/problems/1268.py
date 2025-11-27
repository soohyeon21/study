# 1268

import sys

n = int(sys.stdin.readline())
rec = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

freq = {i:set() for i in range(1, n+1)}
for c in range(5):
    class_student = {}
    for cls in range(1, 10):
        class_student[cls] = class_student.setdefault(cls, [])
    for r in range(n):
        class_student[rec[r][c]].append(r+1)
        
    for cnum, students in class_student.items():
        if (len(students) > 1):
            for student in students:
                freq[student].update(set(students))

tmpcp = sorted(list(freq.items()), key=lambda x:(-len(x[1]), x[0]))[0][0]
print(tmpcp)

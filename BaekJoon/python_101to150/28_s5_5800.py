# 5800

# remove보다는 del이 시간이 덜 드는 것 같다.

# .format()도 써보고 %()도 써봤다.

import sys

k = int(sys.stdin.readline())

class_num = 1
for _ in range(k):
    students = list(map(int, sys.stdin.readline().split()))
    many = students[0]
    #students.remove(many)
    del students[0]
    students.sort()
    #print(many, students)
    max_val = 0
    for i in range(many-1):
        max_val = max(max_val, (students[i+1] - students[i]))
    print("Class %d" %(class_num))
    print("Max {}, Min {}, Largest gap {}" .format(students[many-1], students[0], max_val))
    class_num += 1

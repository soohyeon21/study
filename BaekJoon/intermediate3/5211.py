# 5211

# 악보의 마지막 마디는 하나 이상의 음으로 이루어져 있다. 단지 예시에서 하나의 음만 보여줬을 뿐이다.

import sys

mr = sys.stdin.readline().rstrip().split("|")
cm, am = 0, 0
cmajor = ["C", "F", "G"]
aminor = ["A", "D", "E"]
for bar in mr:
    if (bar[0] in cmajor):
        cm += 1
    elif (bar[0] in aminor):
        am += 1

if (cm > am):
    print("C-major")
elif (cm < am):
    print("A-minor")
elif (cm == am):
    if (mr[-1][-1] in cmajor):
        print("C-major")
    elif (mr[-1][-1] in aminor):
        print("A-minor")

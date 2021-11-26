# 2309

# list.pop[x] # x번째 return하고 삭제
# list.reamove[val] # 앞에 먼저 나오는 val 삭제
# del list[x] # x번째 삭제

# del이 remove보다 걸리는 시간이 적은 듯?

# 틀린 이유는 gnome[mat2]보다 gnome[mat1]을 먼저 삭제해 버려서.
# 런타임 에러는 for문의 local variable인 i, j를 사용해 버려서.

import sys

gnome = []
for _ in range(9):
    gnome.append(int(sys.stdin.readline()))
##print(gnome)

mat1, mat2 = 0, 0
for i in range(8):
    for j in range(i+1, 9):
        if (gnome[i] + gnome[j] == sum(gnome) - 100):
            mat1 = i
            mat2 = j
            break
    if (mat1 != 0):
        break
##if (mat1 < mat2): # 항상 i<j 이므로 필요X
del gnome[mat2]
del gnome[mat1]
##gnome.remove(gnome[mat2]) # same
##gnome.remove(gnome[mat1])

real = sorted(gnome)

for val in real:
    print(val)


#
# Runtime Error(NameError)
# 연속된 두 수만 생각해서 그런가 봄.
#
##import sys
##
##gnome = []
##for _ in range(9):
##    gnome.append(int(sys.stdin.readline()))
##
##for i in range(7):
##    check = gnome[:i] + gnome[i+2:]
##    if (sum(check) == 100):
##        real = sorted(check)
##        break
##
##for real_gnome in real:
##    print(real_gnome)

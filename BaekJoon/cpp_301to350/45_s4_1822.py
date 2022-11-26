# 1822

# 그냥 list와 in을 쓰면 시간초과.
# dictionary가 훨씬 빠르다.

# 증가하는 순으로 출력해야 한다는 조건을 잊지 말자

# print(*sorted(list))
# python은 단순하게 setA-setB 하면 차집합 처리 해주나 보다. # list는 안됨!!
# a = {1, 2, 3} # set
# a = {1:11, 2:22, 3:33} # dictionary
# set은 sort() 사용 불가. 대신 sorted() 사용하면 list가 된다.
# dictionary(해시) # python에서는 dictionary라는 자료구조 통해 해시 제공.

import sys

numa, numb = map(int, sys.stdin.readline().split())
dica, dicb = {}, {}
for n in map(int, sys.stdin.readline().split()):
    dica[n] = 1
for n in map(int, sys.stdin.readline().split()):
    dicb[n] = 1

cnt = 0
fin = []
for num in dica:
    if (num not in dicb):
        cnt += 1
        fin.append(num)

if (not fin):
    print(0)
else:
    print(cnt)
    print(*sorted(fin))

# 1755

# 숫자의 앞글자 하나만 따오면 안된다.
# 앞글자가 같은 경우, 두번째 이후 글자들로도 정렬이 되어야 하기 때문이다.

# 79: "seven" "nine" 따로따로가 아니라 "seven nine" 하나여야 한다. 그래서 틀렸었다.

# sort()하면, " "(공백)이 "a"보다 더 앞이다.

import sys

m, n = map(int, sys.stdin.readline().split())

dic = {}
alp = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
for num in range(m, n+1):
    alphabet = []
    snum = str(num)
    for i in range(len(snum)):
        alphabet += alp[int(snum[i])]+ " "
    dic[num] = alphabet

dlist = list(dic.items())
dlist.sort(key=lambda x:(x[1]))

for j in range(1, len(dlist)+1):
    if (j % 10 == 0):
        print(dlist[j-1][0])
    else:
        print(dlist[j-1][0], end=" ")

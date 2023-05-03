# 10551

#
# sol1) 길게
#
##import sys
##
##l1 = ["`", '1', 'q', 'a', 'z']
##l2 = ['2', 'w', 's', 'x']
##l3 = ['3', 'e', 'd', 'c']
##l4 = ['4', 'r', 'f', 'v', '5', 't', 'g', 'b']
##r4 = ['6', 'y', 'h', 'n', '7', 'u', 'j', 'm']
##r3 = ['8', 'i', 'k', ',']
##r2 = ['9', 'o', 'l', '.']
##r1 = ['0', 'p', ';', '/', '-', '=', '[', ']', "'"]
##
##enter = sys.stdin.readline().rstrip().lower()
##key = [0 for x in range(8)]
##for letter in enter:
##    if (letter in l1):
##        key[0] += 1
##    elif (letter in l2):
##        key[1] += 1
##    elif (letter in l3):
##        key[2] += 1
##    elif (letter in l4):
##        key[3] += 1
##    elif (letter in r4):
##        key[4] += 1
##    elif (letter in r3):
##        key[5] += 1
##    elif (letter in r2):
##        key[6] += 1
##    elif (letter in r1):
##        key[7] += 1
##
##print(*key, sep="\n")



#
# sol2) shorter
# 역시, 더 짧은 풀이가 가능했다.
# 문자는 낱개로 말로 그냥 문자열로 해주자. 어차피 for문으로 하면 낱개로 뜯어 쓰니까!
#
import sys

keyboard = ["`1qaz", '2wsx', '3edc', '4rfv5tgb', '6yhn7ujm', '8ik,', '9ol.', "0p;/'[]-="]

enter = sys.stdin.readline().rstrip().lower()
count = [0 for x in range(8)]

for letter in enter:
    for i in range(8):
        if (letter in keyboard[i]):
            count[i] += 1

print(*count, sep='\n')

# 9226

# "단어에 모음이 없는 경우에도 단어의 끝에 ay만 붙인다."
# 문제를 잘 읽자. 맞는 것 같은데도 틀렸다면, 특이 case가 있는지 살펴보고 input을 넣어 output을 확인해보자.


#
# sol1) 메모리-30840KB, 시간-68ms, 코드 길이-487B
#
import sys

mo = ["a", "e", "i", "o", "u"]

while (1):
    word = sys.stdin.readline().rstrip()
    if (word == "#"):
        break

    if ((mo[0] not in word) and (mo[1] not in word) and (mo[2] not in word) and (mo[3] not in word) and (mo[4] not in word)):
        word += "ay"
    else:
        for i in range(len(word)):
            if (word[0] not in mo):
                word = word[1:] + word[0]
            else:
                word += "ay"
                break
    print(word)


#
# sol2) 메모리-30840KB, 시간-64ms, 코드 길이-388B
#
##import sys
##
##mo = ["a", "e", "i", "o", "u"]
##
##while (1):
##    word = sys.stdin.readline().rstrip()
##    monum = []
##    if (word == "#"):
##        break
##
##    for i in range(5):
##        if (mo[i] in word):
##            monum.append(word.find(mo[i]))
##            
##    if (monum == []):
##        mmin = 0
##    else:
##        mmin = min(monum)
##
##    pig = word[mmin:] + word[:mmin] + "ay"
##    print(pig)

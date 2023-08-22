# 17176

# " ":0, A:1, B:2, ..., Z:26, a:27, b:28, ..., z:52 이런식으로 암호화된다.
# 처음에 각 숫자가 어떤 알파벳을 가리키는지 모른다고 생각하고 문제를 풀어서 틀렸다. (조합이 가능하면 y 출력으로 이해함)
# 흑... 문제를 잘 이해하자.

# dictionary.setdefault(key값, default value값) # default value의 default값은 "None".
# 해당 key의 value값이 없다면 지정해준 default값을 value값으로, value값이 있다면 상관x
# setdefault()를 사용하면 try-except나 if not in을 쓰지 않아도 KeyError를 피할 수 있을듯.

#
# sol1) 내 풀이
#
# 알파벳을 숫자로 바꿔서 dictionary items 비교를 통해 판단하는 풀이
#
##import sys
##
##n = int(sys.stdin.readline())
##cipher = list(map(int, sys.stdin.readline().split()))
##plain = list(sys.stdin.readline().rstrip())
###state = True
##
##cdict = {}
##pdict = {}
##for num in cipher:
##    if (num not in cdict):
##        cdict[num] = 1
##    else:
##        cdict[num] += 1
##for letter in plain:
##    pnum = 0
##    if (letter.isupper()):
##        pnum = ord(letter)-64
##    elif (letter.islower()):
##        pnum = ord(letter)-70
##    
##    if (pnum not in pdict):
##        pdict[pnum] = 1
##    else:
##        pdict[pnum] += 1
##
##cdictval = sorted(cdict.items())
##pdictval = sorted(pdict.items())
##
##if (cdictval == pdictval):
##    print("y")
##else:
##    print("n")


#
# sol2) someone's solution
# 우와 깔끔하다...
#
# 알파벳을 숫자로 바꾸고 각각을 sort하여 비교한 풀이
#
import sys

def init_dict():
    word_dict = {" ":0}
    for i in range(65, 91):
        word_dict[chr(i)] = word_dict.setdefault(chr(i), i-64)
    for j in range(97, 123):
        word_dict[chr(j)] = j-70

    return word_dict

def decoding():
    word_dict = init_dict()
    n = int(sys.stdin.readline())

    cipher_text = sorted(list(map(int, sys.stdin.readline().split())))
    plain_text = sys.stdin.readline().rstrip()
    encode = sorted([word_dict[text] for text in plain_text])

    return 'y' if cipher_text == encode else 'n'

print(decoding())

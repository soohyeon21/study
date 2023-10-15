# 8595

#
# sol1) Python3, PyPy3 모두 시간초과
#
##import sys
##
##n = int(sys.stdin.readline())
##hidden = sys.stdin.readline().rstrip()
##num = ""
##for letter in hidden:
##    if (letter.isdigit()):
##        num += letter
##    else:
##        num += " "
##total = sum(int(strnum) for strnum in num.split())
##print(total)



#
# sol2) replace() 사용하기
#
##import sys
##
##n = int(sys.stdin.readline())
##hidden = sys.stdin.readline().rstrip()
##abc = [chr(A) for A in range(65, 91)] + [chr(a) for a in range(97, 123)]
##
##for letter in abc:
##    hidden = hidden.replace(letter, " ")
##
##total = sum(int(strnum) for strnum in hidden.split())
##print(total)



#
# sol3) 각 자리마다 숫자 or not 파악해서 그에따라 숫자 늘리기 or 끝내고 더해주기
# sol2에 비해 메모리는 절반, 시간은 7배 소요됨.
#
import sys

n = int(sys.stdin.readline())
word = sys.stdin.readline().rstrip()

current_num = 0
total = 0
for letter in word:
    if (letter.isdigit()):
        current_num = current_num*10 + int(letter)
    else:
        total += current_num
        current_num = 0
total += current_num # 마지막에 숫자로 끝나는 경우 처리
print(total)

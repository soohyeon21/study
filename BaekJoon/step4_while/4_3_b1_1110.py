# 1110

# 푸는 아이디어는 비슷한데...
# 맨 처음에 n을 문자로 받느냐, 정수로 받느냐에서 갈린 건가?
# 처음 작성할때는 end = n이었다. str이어서 '01 != 1'되어버려서 계속 돌아갔나보다.

n = input()#'26'
first = n
cycle = 0
end = -1

if (int(n) < 10):
    n = "0" + n

while(end != first):
    a = str(((int(n) // 10) + (int(n) % 10)) % 10)#'8'
    #print(a)
    n = str(int(n) % 10) + a #68
    #print(n)
    end = str(int(n))##
    cycle += 1
print(cycle)


# my 옛날 코드
##n = int(input())
##new = -1
##index = 0
##add = 0
##while (n != new):
##    if (index == 0):
##        new = n
##    add = (new % 10) + int(new / 10); print(add)
##    index += 1
##    newstr = str(int(new % 10)) + str(int(add % 10))
##    new = int(newstr); print(new)
##print(index)

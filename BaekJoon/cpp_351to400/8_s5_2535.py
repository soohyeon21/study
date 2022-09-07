# 2535

# 두 풀이 다 map(int, ) 안해줘서 틀림...

#
# sol1
# dictionary에 없는 값 처리 위해 try-except 사용
#
import sys

n = int(sys.stdin.readline())
competition = []
for _ in range(n):
    competition.append(tuple(map(int, sys.stdin.readline().split())))

competition.sort(key=lambda x:x[2], reverse=True)

##for _ in range(n):
##    print(competition[_])

country = {}
print(competition[0][0], competition[0][1])
country[competition[0][0]] = 1

print(competition[1][0], competition[1][1])
try:
    country[competition[1][0]] += 1
except:
    country[competition[1][0]] = 1

for i in range(2, n):
    try:
        country[competition[i][0]] += 1
        if (country[competition[i][0]] == 2):
            print(competition[i][0], competition[i][1])
##            print("1번만")
            break
        else:
            pass
    except:
        print(competition[i][0], competition[i][1])
##        print("에러생김")
        break


#
# sol2
# KeyError 안나도록 그냥 애초에 dictionary 다 만들어줌.
#
##import sys
##
##n = int(sys.stdin.readline())
##competition = []
##for _ in range(n):
##    competition.append(tuple(map(int, sys.stdin.readline().split())))
##
##competition.sort(key=lambda x:x[2], reverse=True)
##coun = list(set(competition[x][0] for x in range(n)))
##cnt = {}
##for i in range(len(coun)):
##    cnt[coun[i]] = 0
##
####for _ in range(n):
####    print(competition[_])
##
##print(competition[0][0], competition[0][1])
##cnt[competition[0][0]] += 1
##
##print(competition[1][0], competition[1][1])
##cnt[competition[1][0]] += 1
##
##for j in range(2, n):
##    if (cnt[competition[j][0]] < 2):
##        print(competition[j][0], competition[j][1])
##        break
##    else:
##        pass

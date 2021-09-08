# pg.92 #1 큰 수의 법칙

# remove()는 해당 원소 하나만 지우나 보다.

# k번까지 반복 가능하다->제일 큰거 k번+그 다음 큰거 1번 해서 (k+1)크기의 한 세트
# m에 (k+1)이 몇번 들어가나 세어본다. # m // (k + 1)
# 나머지(m % (k + 1))만큼 제일 큰 수의 반복이 일어난다.
# 제일 큰 수와 그 다음 큰 수가 같은 경우를 굳이 분리하여 생각할 필요가 없다.

n, m, k = map(int, input().split())

a = list(map(int, input().split()))
big1 = max(a)
a.remove(big1)
big2 = max(a)
rlt = 0

if (big1 == big2): # 사실 굳이 경우를 나누지 않아도 됨.
    rlt = big1 * m
else: # big1 != big2
    mkset = m // (k + 1)
    mkremain = m % (k + 1)
    rlt = (((big1 * k) + big2) * mkset) + (big1 * mkremain)
print(rlt)

##n, m, k = map(int, input().split())
##
##a = list(map(int, input().split()))
##big1 = max(a)
##a.remove(big1)
##big2 = max(a)
##rlt = 0
##
##mkset = m // (k + 1)
##mkremain = m % (k + 1)
##rlt = (((big1 * k) + big2) * mkset) + (big1 * mkremain)
##print(rlt)

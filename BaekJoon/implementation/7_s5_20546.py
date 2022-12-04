# 20546

# 성민이는 첫날부터 주식을 매수하지 않는다. 무조건 3일의 데이터를 봐야만 매수/매도를 할 수 있다.

# 성민이는 연속 4일째에 action을 취하지 않는다.
# 전날보다 가격이 올랐기 때문에 남은 돈으로는 살 수 없다. 마찬가지로 전날보다 가격이 떨어졌어도 어차피 팔 주식이 없다.
# 그리고 어차피 '전량' 매수/매도이다. 이미 보유한 상태에서 추가 매수 하는 것은 원칙에 어긋나는 일이 된다.

import sys

def joon(cash, stock):
    stnum = 0
    leftcash = cash
    for val in stock:
        tmp = leftcash//val
        leftcash -= tmp*val
        stnum += tmp
    return stnum*stock[13]+leftcash

def sung(cash, stock):
    stnum = 0
    leftcash = cash
    up, down = 0, 0
    before = stock[0]
    for i in range(1, 14):
        if (stock[i] > before):
            up += 1
            down = 0
        elif (stock[i] < before):
            down += 1
            up = 0
        else:
            down = 0
            up = 0

        if (up == 3):
            leftcash += stock[i]*stnum
            stnum = 0
            up = 0
        elif (down == 3):
            tmp = leftcash//stock[i]
            leftcash -= tmp*stock[i]
            stnum += tmp
            down = 0
    return stnum*stock[13]+leftcash
        

cash = int(sys.stdin.readline())
stock = list(map(int, sys.stdin.readline().split()))

joonc = joon(cash, stock)
sungc = sung(cash, stock)
if (joonc > sungc):
    print("BNP")
elif (joonc < sungc):
    print("TIMING")
else:
    print("SAMESAME")

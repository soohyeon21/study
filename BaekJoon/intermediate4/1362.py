# 1362

# w에 대한 판단은 마지막에만 해도 충분하다.
# class를 이용한 풀이도 깔끔한듯.

import sys

cnt = 1
while (1):
    o, w = map(int, sys.stdin.readline().split())
    if ((o==0) and (w==0)):
        break

    live = True
    state = ""
    while (1):
        a, n = sys.stdin.readline().split()
        if (a == "#"):
            print(cnt, end=" ")
            if (live):
                print(state)
            else:
                print("RIP")
            cnt += 1
            break

        if (a == "E"):
            w -= int(n)
        elif (a == "F"):
            w += int(n)

        if (o/2 < w < 2*o):
            state = ":-)"
        elif (w <= 0):
            live = False
        else:
            state = ":-("


#
# someone's sol)
#
##import sys
##
##class Pet:
##    def __init__(self, o, w):
##        self.o = o
##        self.w = w
##        self.is_alive = True
##
##    def action(self, typeof, value):
##        if typeof == 'F':
##            self.w += value
##        elif typeof == 'E':
##            self.w -= value
##
##        if self.w <= 0:
##            self.is_alive = False
##
##    def state(self):
##        if not self.is_alive:
##            return 'RIP'
##        elif self.o * 0.5 < self.w < self.o * 2:
##            return ':-)'
##        else:
##            return ':-('
##
##
##if __name__ == '__main__':
##    count = 0
##    while True:
##        o, w = map(int, input().split())
##        if o == 0 and w == 0:
##            break
##
##        pet = Pet(o, w)
##        count += 1
##
##        while True:
##            typeof, value = sys.stdin.readline().split()
##            if typeof == '#' and value == '0':
##                print(count, pet.state())
##                break
##
##            pet.action(typeof, int(value))

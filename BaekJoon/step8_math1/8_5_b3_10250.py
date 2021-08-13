# 10250

# 확인을 위해 가로세로 한 줄씩 넣어서 확인해보자.
# +  print(f'{}') # {}안의 변수를 여러번 출력. 매번 값이 달라질 수 있음.

t = int(input())

for i in range(t):
    h, w, n = map(int, input().split())

    quo = n // h
    rem = n % h

    if (rem == 0):
        quo -= 1
        rem = h
    
    if (quo < 9):
        xx = "0" + str(quo + 1)
    else: # quo >= 9
        xx = str(quo + 1)
        
    room = str(rem) + xx
    
    print(room)

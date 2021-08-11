# 10951

# 둘 다 맞는 풀이.
# sys.stdin or try-except
# for 반복문 내부의 sys.stdin은 표준 입력에 대한 반복.
# 값이 존재하면 계속 반복되며, 강제 종료인 'ctrl + z'를 누르면 종료됨.


##import sys
##
##for value in sys.stdin:
##    a, b = map(int, value.split()) # value 대신 sys.stdin은 안됨.
##    print(a + b)

#
#

while(1):
    try:
        a, b = map(int, input().split())
        print(a + b)
    except:
        break

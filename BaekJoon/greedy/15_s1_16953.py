# 16953 A → B

# 다른 사람의 심플한 풀이를 보고 나니 내 코드가 참...
# 아냐 그래도 풀었잖아. 잘했어.

# def 안에서 return (값)을 하는데 왜 자꾸 (값)이 return이 안되고
# None 값만 return하는 것인지 모르겠다. return 뒤에 값 줬잖아!!
# 그래서 그냥 def 안에 print() 넣고, 함수 실행만 하고 print(cal())은 안해줬다.

# 부디 다음에 다시 풀 때는 깔끔하게 풀 수 있었으면 좋겠다.

def cal(a, b, cnt):
    if (a == b):
        print(cnt)
        return
    elif (a > b):
        print(-1)
        return

    ones = b % 10

    if (ones == 1):
        b = str(b)
        b = int(b[:len(b) - 1])
        cnt += 1
        cal(a, b, cnt)
    elif (ones % 2 == 0):
        b //= 2
        cnt += 1
        cal(a, b, cnt)
    else: # ones가 1이 아닌 홀수
        print(-1)

A, B = map(int, input().split())

cal(A, B, 1)


# 누군가의 코드. 참 심플하게도 풀었다...
##A, B = map(int,input().split())
##answer = 1
##while True:
##    if B % 2 == 0:
##        B = B / 2
##    else:
##        B -= 1
##        B /= 10
##    answer += 1
##    if B <= A:
##        break
##
##if B < A:
##    print(-1)
##else:
##    print(answer)

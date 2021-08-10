# 2292

# 어떤 식으로 작동하는지, 지나가는 방의 수의 규칙을 찾아보도록 하자.
# 굳이 1, 7, 19, 37, ...의 일반항을 구할 필요까지는 없었다.
# 그래도 결과적으론 잘 파악했으니, 일단은 칭찬!!


# 베껴온 코드
##n = int(input())
##
##nums_pileup = 1  # 벌집의 개수, 1개부터 시작
##cnt = 1
##while n > nums_pileup :
##    nums_pileup += 6 * cnt  # 벌집이 6의 배수로 증가
##    cnt += 1  # 반복문을 반복하는 횟수
##print(cnt)

# 일반항 구해서 내가 직접 생각한 코드
n = int(input())
r = 1
more = True # 계속 작업하시오

if (n == r):
    print(r)
else:
    r += 1
    while (more):
        if (((3*(r - 1)**2 - 3 * (r - 1) + 1) < n) and (n <= (3*r**2 - 3*r +1))):
            print(r)
            more = False
        else:
            r += 1

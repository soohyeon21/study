# 13305 주유소

# 너무 복잡하게 생각해버렸다.
# case를 합칠 수는 없는지, 더 간단한 방법은 없는지 생각하며 풀자.
# 아마 python은 감당 가능한 수 범위가 더 넓어서 큰 문제 없는듯?
# 처음에 작성한 코드는 어떤 부분이 부족한 걸까...

# list1 = list; list2 = list1.sort();를 하면 list를 출력해도 sort되어 있음.
# list1과 list는 단지 동일 [원소1, 원소2, ..., 원소n]을 가리키는 이름일 뿐.
# list2 = sorted(list1)을 해야 list1과 list2의 값이 다름.

# 전체 길이 만큼의 기름을 사야한다.
# 만약 값이 모두 동일하다면, 한꺼번에 구매하면 된다.
# 만약 갈수록 값이 비싸진다면, 처음에 한꺼번에 구매하면 된다.
# 만약 갈수록 값이 싸진다면, 필요한 만큼씩만 구매하면 된다.
# 만약 값이 순서 없이 뒤죽박죽이라면...
# 일단 시작할땐 첫 거리만큼은 반드시 사야 한다.
# 구매시에는 자신보다 싼 도시에 도달할때까지 필요한 기름을 사야한다.


# 100/100점. 164ms
n = int(input()) # 도시 개수
km = list(map(int, input().split())) # 도로 길이
lit = list(map(int, input().split())) # 주유소 리터당 가격
price = 0 # 최종 지불 비용

minVal = lit[0]
for i in range(len(lit) - 1):
    if (minVal > lit[i]):
        minVal = lit[i]
    price += minVal * km[i]
print(price)



# 17/100점. 124ms
##n = int(input()) # 도시 개수
##km = list(map(int, input().split())) # 도로 길이
##lit = list(map(int, input().split())) # 주유소 리터당 가격
##price = 0 # 최종 지불 비용
##
##lit_s = sorted(lit)
##lit_r = lit_s.reverse()
##
##if (len(set(lit)) == 1): # 가격 동일
##    price = sum(km) * lit[0]
##elif (lit == lit_s): # 갈수록 비싸짐
##    price = sum(km) * lit[0]
##elif (lit == lit_r): # 갈수록 싸짐
##    for i in range(len(km)):
##        price += km[i] * lit[i]
##else: # 값이 뒤죽박죽
##    st =  lit[0]
##    buy = km[0]
##    for i in range(len(lit) - 1):
##        if ((i + 1) == len(lit) - 1):
##            buy += km[-1]
##        elif (st <= lit[i + 1]): # 갈수록 비싸짐/그대로
##            buy += km[i]
##        else: # 갈수록 싸짐
##            price += buy * st
##            st = lit[i + 1]
##            buy = 0
####    buy += km[-1]
##    price += buy * st
##
##print(price)



# 17/100점. 120ms
##n = int(input()) # 도시 개수
##km = list(map(int, input().split())) # 도로 길이
##lit = list(map(int, input().split())) # 주유소 리터당 가격
##price = 0 # 최종 지불 비용
##
##lit_s = sorted(lit)
##lit_r = lit_s.reverse()
##
##if (len(set(lit)) == 1): # 가격 동일
##    price = sum(km) * lit[0]
##elif (lit == lit_s): # 갈수록 비싸짐
##    price = sum(km) * lit[0]
##elif (lit == lit_r): # 갈수록 싸짐
##    for i in range(len(km)):
##        price += km[i] * lit[i]
##else: # 값이 뒤죽박죽
##    st =  lit[0]
##    buy = km[0]
##    for i in range(len(lit) - 2):
####        if ((i + 1) == len(lit) - 1):
####            buy += km[-1]
##        if (st <= lit[i + 1]): # 갈수록 비싸짐/그대로
##            buy += km[i]
##        else: # 갈수록 싸짐
##            price += buy * st
##            st = lit[i + 1]
##            buy = 0
##    buy += km[-1]
##    price += buy * st
##
##print(price)


# 누군가의 code
##N = int(input())
##roads = list(map(int, input().split()))
##cities = list(map(int, input().split()))
##
##minVal = cities[0]
##sum = 0
##for i in range(N-1):
##    if minVal > cities[i]:
##        minVal = cities[i]
##    sum += (minVal * roads[i])
##    
##print(sum)

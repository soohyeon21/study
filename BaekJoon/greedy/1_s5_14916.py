# 14916 거스름돈

# 경우의 수를 잘 나누어야 될 듯 하다.
# 이 문제는 특이하게도, 거스름돈의 단위가 배수 관계에 있지 않다.

# 거스름돈이 5의 배수/5로 나눈 나머지가 짝수/5로 나는 나머지가 홀수&여분의 5 있음/
# 5로 나눈 나머지가 홀수&여분의 5 없음(-1 출력 경우) 이렇게 4가지 경우가 있다.

change = int(input())
num = 0

if (change % 5 == 0): # 5의 배수
    num += change // 5
elif ((change % 5) % 2 == 0): # 5로 나눈 나머지가 짝수
    num += change // 5
    change %= 5
    num += change // 2
elif (change // 5 > 0): # 5로 나눈 나머지가 홀수_여유분 5 있음
    num += (change // 5) - 1
    change = (change % 5) + 5
    num += change // 2
else: # 5로 나눈 나머지가 홀수_여유분 5 없음
    num = -1
print(num)

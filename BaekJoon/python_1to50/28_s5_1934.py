# 1934

# 유클리드 호제법(互除法)_Euclidean Algorithm
#
# a를 b로 나눈 나머지를 r이라 할 때,
# a, b의 최대공약수는 b, r의 최대공약수이다.
# =>(a, b의 최대 공약수 == a%b의 최대공약수)
# (a % b == 0)일 때의 b 값이 최대공약수.
# (혹은 b == 0일 때의 a 값이 최대공약수)

# if b: # b가 0인 경우 False, 그 외 True 인듯.

def gcf(a, b):
    while (b != 0):
        r = a % b
        a = b
        b = r
    return a

def gcf_r(a, b):
    if (b != 0):
        return gcf_r(b, a%b)
    else:
        return a
    #return gcf_r(b, a%b) if b else a # can be shorten like this

def lcm(a, b):
    return (a * b // gcf(a, b))
    #return (a * b // gcf_r(a, b)) # same



t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
##    factor = gcf(a, b) # 3 lines instead when not using lcm()
##    lcmm = factor * (a // factor) * (b // factor)
##    print(lcmm)
    print(lcm(a, b))

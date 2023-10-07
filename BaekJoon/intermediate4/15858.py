# 15858

# a*b/c는 50점
# 직접 나눗셈 과정을 구현해야한다. 소수점 아래 최소 6개 자리까지.

# float 연산은 컴퓨터 관점의 이진수 기반 연산이기 때문에 미세한 연산의 오류 발생 가능.
# (python float 기본 타입은 대부분의 다른 프로그래밍 언어들처럼 소수를 내부적으로 이진수의 형태로 저장하기 때문.)
# 따라서, 정확한 십진수 기반의 연산이 필요한 경우에는 내장 모듈 decimal을 사용하는 것이 좋음.
# 대신 decimal.Decimal()을 사용할 때는 생성자에 숫자 대신 문자열을 줘야 함.
#
# ex)
# 1.1+2.2
# >>> 3.3000000000000003
# float(1.1) + float(2.2)
# >>> 3.3000000000000003
# import decimal
# decimal.Decimal('1.1') + decimal.Decimal('2.2')
# >>> Decimal('3.3')
# decimal.Decimal(1.1) + decimal.Decimal(2.2)
# >>> Decimal('3.30000000000000026645353')

#
# sol1) 나눗셈 직접 구현
#
##import sys
##
##a, b, c = map(int, sys.stdin.readline().split())
##ab = a*b
##ans = str(ab//c)+"."
##for i in range(6): # 10**(-6) 이내여야 하므로 최소 6번은 계산 필요
##    ab = ab%c * 10
##    ans += str(ab//c)
##
##print(ans)


#
# sol2) from decimal import Decimal, getcontext
#
# 메모리와 시간 모두 sol1에 비해 아주 약간 더 소모되기는 함.
# prec ~ 7: 틀림
# prec ~10: 25점
# prec ~17: 50점
# prec 24~: 100점
# 정밀도(prec)는 소수부분+정수부분 자릿수를 모두 포함하여 알려준다.
# (ex: prec=3 -> 12.3, 1.12, 0.123)
# 서브태스크4의 조건이 1<=a,b,c<=10**9로, 10**9이기 때문에 prec=24부터 100점 처리되는게 아닐까, 하는 내 생각.
#
##from decimal import Decimal, getcontext
##import sys
##
##getcontext().prec = 24
##a, b, c = map(Decimal, sys.stdin.readline().split())
##print(a*b/c)


#
# sol3) decimal.Decimal()만 사용
#
# decimal.getcontext().prec 사용하지 않아도 100점이기는 함.
# -> decimal.getcontext().prec의 default 값은 24이기 때문.
#
from decimal import Decimal, getcontext
import sys

a, b, c = map(Decimal, sys.stdin.readline().split())
print(a*b/c)

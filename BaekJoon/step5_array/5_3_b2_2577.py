#2577

# 다른 방법도 언제나 존재한다.
# 비슷하게 반복되는 건 반복문도 고려해보자.

a = int(input())
b = int(input())
c = int(input())

m = str(a * b * c)
ls = []
for i in range(len(m)):
    ls.append(m[i])
#print(ls)
print(ls.count('0'))
print(ls.count('1'))
print(ls.count('2'))
print(ls.count('3'))
print(ls.count('4'))
print(ls.count('5'))
print(ls.count('6'))
print(ls.count('7'))
print(ls.count('8'))
print(ls.count('9'))


# simpler way
##a = int(input())
##b = int(input())
##c = int(input())
##
##arr = list(str(a * b * c))
##for i in range(10):
##    print(arr.count(str(i)))

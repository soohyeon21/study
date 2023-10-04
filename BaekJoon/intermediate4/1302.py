# 1302

#
# sol1) in 사용
#
##import sys
##
##n = int(sys.stdin.readline())
##book = {}
##for _ in range(n):
##    name = sys.stdin.readline().rstrip()
##    if (name in book):
##        book[name] += 1
##    else:
##        book[name] = 1
##
##order = sorted(book.items(), key=lambda x:(-x[1], x[0]))
##print(order[0][0])


#
# sol2) dict.setdefault(KEY, default) 사용
#
import sys

n = int(sys.stdin.readline())
book = {}
for _ in range(n):
    name = sys.stdin.readline().rstrip()
    book[name] = book.setdefault(name, 0)
    book[name] += 1

order = sorted(book.items(), key=lambda x:(-x[1], x[0]))
print(order[0][0])

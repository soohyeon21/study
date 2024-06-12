# 13986

# for i in reversed(range(3)): # i는 2, 1, 0 순서

#
# sol1) 맞았으나, 아주 맘에 들지는 않는 풀이.
#
##import sys
##
##n, m = map(int, sys.stdin.readline().split())
##
##latit = [[] for _ in range(m)]
##result = []
##for _ in range(n):
##    line = sys.stdin.readline().rstrip()
##    for i in range(m):
##        latit[i].append(line[i])
##
##for j in range(m):
##    one = latit[j]
##    stack = ["#", one.pop()]
##    tmp = []
##    for k in range(n-1):
##        now = one.pop()
##        if (now == "o"):
##            for s in range(len(stack)):
##                if (stack[-1] == "."): # 여기 때문에 처음에 stack에 "#" 추가함
##                    tmp.append(stack.pop())
##                else:
##                    stack.append(now)
##                    for t in range(len(tmp)):
##                        stack.append(tmp.pop())
##                    break
##        else:
##            stack.append(now)
##    stack.pop(0)
##    result.append(stack)
##
##for p in range(n):
##    for q in range(m):
##        print(result[q][n-p-1], end="")
##    print()



#
# sol2) 누군가의 풀이. 우와...
#
import sys

def gravity(n, m, grid):
    for col in range(m):
        empty_spaces_below = 0
        for row in reversed(range(n)):
            if (grid[row][col] == 'o'):
                grid[row][col] = '.'
                grid[row + empty_spaces_below][col] = 'o'
            elif (grid[row][col] == '.'):
                empty_spaces_below += 1
            else:
                empty_spaces_below = 0
    return grid

n, m = map(int, sys.stdin.readline().split())
grid = [list(sys.stdin.readline().rstrip()) for _ in range(n)]

after_gravity = gravity(n, m, grid)

for one in after_gravity:
    print(*one, sep='')

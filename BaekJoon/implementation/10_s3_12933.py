# 12933

# a = [*input()] # ["a", "b", "c", "d", "e"]으로 알파벳별로 바로 분리 가능.

import sys

def duck(lst):
    quack = "quack"
    dcnt = 0
    idx1, idx2 = 0, 0 # 절대, 상대
    for i in range(len(lst)//5):
        for j in range(5):
            try:
                idx2 = lst[idx1+idx2:].index(quack[j])
                idx1 += idx2
                idx2 = 0
                lst[idx1] = 0
            except:
                return -1
##            print(*lst, idx1, sep='')
            try:
                tmp = lst[idx1+idx2:].index(quack[(j+1)%5])
            except ValueError:
                if (quack[(j+1)%5] == "q"):
                    dcnt += 1
                    idx1, idx2 = 0, 0
##            print(*lst, idx1, sep='')

    return dcnt


cry = sys.stdin.readline().rstrip()
cryl = [x for x in cry]

num = len(cry)//5
if ((cryl.count('q') == num) and (num == cryl.count('u')) and (num == cryl.count('a')) and (num == cryl.count('c')) and (num == cryl.count('k'))):
    print(duck(cryl))
else:
    print(-1)


###
### 누군가의 풀이. 마지막 if-else indentation 때문에 돌아갈지는 모르겠지만,
### 일단 맞은 풀이라고 하니.. search 공부하고 나면 더 이해할 수 있으려나
###
##import sys
##
##input = sys.stdin.readline
##
##sound = [*input().rstrip()]
##quack = 'quack'
##N = len(sound)
##visited = [0]*N
##idx = 0
##for i in range(N//5):
##    for j in range(N):
##        if not visited[j]:
##            if sound[j] == quack[idx]:
##                idx = (idx+1)%5
##                visited[j] = i+1
##    if visited.count(i+1)%5:
##        print(-1)
##        break
##else:
##    print(-1) if 0 in visited else print(max(visited))

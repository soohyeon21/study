# 9946

# sort를 써서 푸는 방법도 있다.

#
# sol1) 시간초과
#
##import sys
##
##cnt = 1
##status = ""
##while (1):
##    puzzle = sys.stdin.readline().rstrip()
##    back = list(sys.stdin.readline().rstrip())
##    if (puzzle == "END"):
##        break
##
##    for i in range(len(puzzle)):
##        if (puzzle[i] in back):
##            back[back.index(puzzle[i])] = 0
##        else:
##            back.append(-1)
##    if ((back.count(0) != len(puzzle)) or (len(back) != len(puzzle))):
##        status = "different"
##    else:
##        status = "same"
##    print("Case {}: {}" .format(cnt, status))
##    cnt += 1


#
# sol2) 성공
#
import sys

cnt = 1
while (1):
    status = "initial"
    puzzle = sys.stdin.readline().rstrip()
    back = list(sys.stdin.readline().rstrip())
    if (puzzle == "END"):
        break

    pset = set(puzzle)
    for puz in pset:
        if (puzzle.count(puz) != back.count(puz)):
            status = "different"
            break
    if (status == "initial"):
        status = "same"
    print("Case {}: {}" .format(cnt, status))
    cnt += 1
            

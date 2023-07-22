# 10410

# if 여러개 vs if-elif-else

# "Thus, a student who has completed 41 courses or more is considered to have more than 8 semesters of full-time study."
# "41 courses or more" # 놓치지 말고 읽자.

#
# sol1)
#
##import sys
##
##t = int(sys.stdin.readline())
##for _ in range(t):
##    name, post, birth, courses = sys.stdin.readline().split()
##    state = ""
##    
##    if (int(post[:4]) >= 2010):
##        state = "eligible"
##    if (int(birth[:4]) >= 1991):
##        state = "eligible"
##    if ((state == "") and (int(courses) >= 41)):
##        state = "ineligible"
##    if (state == ""):
##        state = "coach petitions"
##
##    print(name, state)


#
# sol2)
#
import sys

t = int(sys.stdin.readline())
for _ in range(t):
    name, post, birth, courses = sys.stdin.readline().split()
    state = ""
    
    if ((int(post[:4]) >= 2010) or (int(birth[:4]) >= 1991)):
        state = "eligible"
    elif (int(courses) >= 41):
        state = "ineligible"
    else:
        state = "coach petitions"

    print(name, state)

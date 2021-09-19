# 1343 폴리오미노

# 나름 경우를 잘 나누어 풀었다고 생각한다만,
# replace()를 활용하면 훠얼씬 더 간단하게 접근 가능하다.

# [:]의 형태는 문자열 slicing뿐만 아니라, 리스트에서도 사용 가능한 듯.
# 문자열 slicing에서 원본을 바꾸는 것은 불가능하다.
# 그래서 여기서도 문자열 ex1을 베껴온 리스트 ex를 사용하여 X를 A/B로 대체하였다.

# X가 연속되는 갯수에 따라 -1을 출력/A만 출력/B만 출력/AB 섞어서 출력.
# AB를 섞어서 출력하는 경우, B는 2개, A는 4개이므로
# B가 나오는 경우는 기껏해야 끝에 두자리가 다다.
# 마지막에 연속한 X는 바꿔주지 못한다. 
# 그래서, 해결책으로 처음에 끝에 "."을 덧붙이고,
# 나중에 맨 끝의 "."를 제하는 방식을 사용하였다.

ex1 = input() + "."
ex = []

for letter in ex1:
    ex.append(letter)

cnt = 0
result = ""

for i in range(len(ex)):
    if (ex[i] == "X"):
        cnt += 1
    elif (cnt % 2 != 0): # 홀수인 경우 -1 출력
        ex = "-1"
        cnt = 0
        break
    elif (cnt % 4 == 0): # (ex[i] == ".") & AAAA
        ex[(i - cnt):i] = "AAAA" * (cnt // 4)
##        for j in range(i - cnt, i):
##            ex[j] = "A"
        cnt = 0
    elif (cnt == 2): # (ex[i] == ".") & BB
        ex[(i - cnt):i] = "BB"
        cnt = 0
    else: # (ex[i] == ".") & (AAAA + BB) # 2의 배수
        ex[(i - cnt):(i - 2)] = "AAAA" * (cnt // 4)
        ex[(i - 2):i] = "BB"
        cnt = 0
if (ex == "-1"):
    print(-1)
else:
    answer = ""
    for k in range(len(ex) - 1):
        answer += str(ex[k])
    print(answer)


# someone's code
# 정말 심플한듯...
#
##s = input()
##s = s.replace("XXXX", "AAAA")
##s = s.replace("XX", "BB")
##
##if "X" in s:
##    print(-1)
##else:
##    print(s)



# 초기 아이디어
##string = list(input().split("."))
##print(string)
##
##ready = []
##result = ""
##for element in string:
##    if (element != ''):
##        ready.append(element)
##
##print(ready)
##
##for ele in ready:
##    if (len(ele) % 2 != 0): # 홀수이면
##        result = "-1"

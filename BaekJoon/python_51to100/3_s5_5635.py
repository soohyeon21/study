# 5635

# lambda 쓰면 매우 간단히 해결되는 듯ㅎ

# 맞긴 맞았지만... 과연 잘 풀은 code라고는 할 수 있을까??
# 오잉 oldest()는 맞지만, youngest()는 틀린 것 같은 걸?

# def의 parameter로 min/max를 주고 parameter() 이렇게 하면
# max()/min() 효과가 날 줄 알았는데, 안된다ㅎㅎ
# 그래서 비슷한 부분이 있는데도 def 또 만들어서 간결히 못하겠음...

import sys

name = []
day = []
month = []
year = []

##def pick_me(state, date, n, date2, value):
##    buf = []
##    if (date.count(state(date)) != 1):
##        for dates in range(n):
##            if (date[dates] == state(date)):
##                buf.append(dates)
##        for k in range(n):
##            if (k not in buf):
##                date2[k] = value

def youngest():
    if (year.count(max(year)) != 1): # 나이 가장 적은 사람이 여럿
        y_buf = [] # 나이 적은 애들 연도 index
        m_buf = [] # 나이 어린 애들 달 index
        # 가장 어린데, 같은 연도 출생
        for years in year:
            if (years == max(year)):
                y_buf.append(year.index(years))
        for i in range(n): # 가장 어리지 않으면 배제.
            if (i not in y_buf):
                month[i] = 0
                
        if (month.count(max(month)) != 1): # 어린데, 같은 달 출생 있음.
            for months in month:
                if (months == max(month)): # 같은 달 출생
                    m_buf.append(month.index(months))
            for j in range(n): # day 비교할 애들만 남기기.
                if (j not in m_buf):
                    day[j] = 0
                    
            pick = day.index(max(day))
                
        else: # 연도-달 비교했을 때 혼자만 어림
            pick = month.index(max(month))

    else: # 연도 비교했을 때 혼자만 어림
        pick = year.index(max(year))

    return name[pick]

def oldest():
    if (year.count(min(year)) != 1): # more than one same year
        y_buf = [] # 나이 많은 애들 연도 index
        m_buf = [] # 나이 많은 애들 달 index
        # 가장 old, 같은 연도 출생
        for years in range(n):
            if (year[years] == min(year)):
                y_buf.append(years)
        for i in range(n): # 가장 old 않으면 배제.
            if (i not in y_buf):
                month[i] = 100
                
        if (month.count(min(month)) != 1): # old, 같은 달 출생 있음.
            for months in range(n):
                if (month[months] == min(month)): # 같은 달 출생
                    m_buf.append(months)
            for j in range(n): # day 비교할 애들만 남기기.
                if (j not in m_buf):
                    day[j] = 100
                    
            pick = day.index(min(day))
                
        else: # 혼자만 old
            pick = month.index(min(month))

    else: # one least year
        pick = year.index(min(year))

    return name[pick]

n = int(sys.stdin.readline())

for _ in range(n):
    nn, dd, mm, yy = sys.stdin.readline().split()
    name.append(nn)
    day.append(int(dd))
    month.append(int(mm))
    year.append(int(yy))

print(youngest())
print(oldest())


#
#
## lambda 사용 code
li = []
for _ in range(int(input())):
    n, d, m, y = input().split()
    li.append([n, int(d), int(m), int(y)])
li.sort(key=lambda x:(x[3],x[2],x[1]))
print(li[-1][0])
print(li[0][0])

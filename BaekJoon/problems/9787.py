# 9787

import sys

country = []
while (1):
    ipt = sys.stdin.readline().rstrip()
    if (ipt == ''):
        break
    name, *medals = ipt.split()
    country.append([name, list(map(int, medals))])

country.sort(key=lambda x:(-x[1][0], -x[1][1], -x[1][2]))
country[0].append(1)
for i in range(1, len(country)):
    if (country[i][1] == country[i-1][1]):
        country[i].append(country[i-1][2])
    else:
        country[i].append(i+1)
country.sort(key=lambda x:(x[2], x[0]))

for k in range(len(country)):
    print(f"{country[k][2]} {country[k][0]}", *country[k][1], sum(country[k][1]))

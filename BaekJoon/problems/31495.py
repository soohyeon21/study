# 31495

# count() 대신 len(s)>2 조건을 넣으면 inner을 고려하지 않아도 됨.

import sys

s = sys.stdin.readline().rstrip()

result = 'CE'
if ((s.count('"') == 2) and (s[0] == '"') and (s[-1] == '"')):
    inner = s.replace('"', '')
    if (inner != ''):
        result = inner

print(result)

# 18238

import sys

string = sys.stdin.readline().rstrip()
start = 0
cnt = 0

for letter in string:
    #print(chr(start+65), cnt)
    cnt += min(abs(start-(ord(letter)-65)), abs(min(start, ord(letter)-65)+26 - max(start, ord(letter)-65)))
    start = ord(letter)-65

print(cnt)

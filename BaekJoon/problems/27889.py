# 27889

import sys

school = {'NLCS':'North London Collegiate School', 'BHA':'Branksome Hall Asia', 'KIS':'Korea International School', 'SJA':'St. Johnsbury Academy'}

abb = sys.stdin.readline().rstrip()
print(school[abb])

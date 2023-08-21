# 17284

import sys

button = sys.stdin.readline().split()
rest = 5000 - button.count("1")*500 - button.count("2")*800 - button.count("3")*1000
print(rest)

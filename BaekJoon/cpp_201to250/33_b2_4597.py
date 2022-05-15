# 4597

import sys

while (1):
    string = sys.stdin.readline().rstrip()
    if (string == "#"):
        break

    cnt1 = string[:len(string)-1].count("1")
    if ((string[-1] == "e") and (cnt1 % 2 == 0)):
        news = string[:len(string)-1] + "0"
    elif ((string[-1] == "e") and (cnt1 % 2 == 1)):
        news = string[:len(string)-1] + "1"
    elif ((string[-1] == "o") and (cnt1 % 2 == 0)):
        news = string[:len(string)-1] + "1"
    elif ((string[-1] == "o") and (cnt1 % 2 == 1)):
        news = string[:len(string)-1] + "0"

    print(news)

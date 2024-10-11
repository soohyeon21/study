# 13288

import sys

trans = {'a':'@', 'b':'8', 'c':'(', 'd':'|)', 'e':'3', 'f':'#', 'g':'6',
         'h':'[-]', 'i':'|', 'j':'_|', 'k':'|<', 'l':'1', 'm':'[]\/[]',
         'n':'[]\[]', 'o':'0', 'p':'|D', 'q':'(,)', 'r':'|Z', 's':'$',
         't':"']['", 'u':'|_|', 'v':'\/', 'w':'\/\/', 'x':'}{', 'y':'`/', 'z':'2'}

ipt = sys.stdin.readline().replace("\n", '')

rst = ""
for letter in ipt:
    if (letter.isalpha()):
        rst += trans[letter.lower()]
    else:
        rst += letter

print(rst)

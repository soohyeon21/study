# 6474

import sys

reverse_t = {}
rpair = ['E3', 'JL', 'S2', 'Z5']
rsame = 'AHIMOTUVWXY18'
for one in rpair:
    reverse_t[one[0]] = one[1]
    reverse_t[one[1]] = one[0]
for one in rsame:
    reverse_t[one] = one

while (1):
    string = sys.stdin.readline().rstrip()
    if (string == ''):
        break

    isPal = True
    if (string != string[::-1]):
        isPal = False

    isMirr = False
    reverse = ''
    for letter in string:
        try:
            reverse += reverse_t[letter]
        except KeyError:
            reverse += '&'
    if (reverse == string[::-1]):
        isMirr = True

    notw = ""
    which = ''
    if (isPal and isMirr):
        which = 'mirrored palindrome'
    elif (isMirr):
        which = "mirrored string"
    elif (isPal):
        which = 'palindrome'
    elif ((not isPal) and (not isMirr)):
        notw = 'not '
        which = 'palindrome'

    print(f"{string} -- is {notw}a {which}.\n")

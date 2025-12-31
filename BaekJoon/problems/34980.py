# 34980

import sys

n = int(sys.stdin.readline())
morning = sys.stdin.readline().rstrip()
night = sys.stdin.readline().rstrip()

m_bottle = morning.count('w')
n_bottle = night.count('w')

state = 'Oryang'
if (m_bottle < n_bottle):
    state = 'Manners maketh man'
elif (m_bottle == n_bottle):
    if (morning == night):
        state = 'Good'
    else:
        state = 'Its fine'

print(state)

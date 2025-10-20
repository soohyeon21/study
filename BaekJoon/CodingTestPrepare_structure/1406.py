# 1406

# list.insert() # O(n)

#
# sol1) python3, pypy3 시간초과
#
##import sys
##
##def doWork(order, lst, cursor):
##    if (order[0] == 'L'):
##        cursor = max(0, cursor-1)
##    elif (order[0] == 'D'):
##        cursor = min(len(lst), cursor+1)
##    elif (order[0] == 'B'):
##        if (cursor != 0):
##            lst.pop(cursor-1)
##            cursor -= 1
##    elif (order[0] == 'P'):
##        lst.insert(cursor, order[1][0])
##        cursor += 1
##
##    return lst, cursor
##        
##
##editor = list(sys.stdin.readline().rstrip())
##m = int(sys.stdin.readline())
##
##order = []
##for _ in range(m):
##    a, *b = sys.stdin.readline().split()
##    order.append((a, b))
##
##cursor = len(editor)
##for single_order in order:
##    editor, cursor = doWork(single_order, editor, cursor)
##
##print(''.join(editor))



#
# sol2
#
import sys

def doWork(order, cursor, nord): # order=('P', ['y']), ('L', [])
    print(f"NOW cur: {cursor}")
    if (order[0] == 'L'):
        if (llst[cursor][0] != None):
            cursor = llst[cursor][0]
    elif (order[0] == 'D'):
        if (llst[cursor][2] != None):
            cursor = llst[cursor][2]
    elif (order[0] == 'B'):
        llst[llst[cursor][0]][2] = llst[cursor][2]
        llst[llst[cursor][2]][0] = llst[cursor][0]
        llst.pop(cursor)
    elif (order[0] == 'P'):
        llst[nord] = [cursor, order[1][0], llst[cursor][2]]
        llst[llst[cursor][2]][0] = nord
        llst[cursor][2] = nord
        cursor = nord
    print(cursor, order, llst)

    return cursor


editor = sys.stdin.readline().rstrip()
m = int(sys.stdin.readline())

llst = {0:[None, '', 1]}
llst.update({i:[i-1, editor[i-1], i+1] for i in range(1, len(editor)+1)})
llst.update({len(editor)+1:[len(editor), '', None]})

cursor = len(editor)
for nord in range(len(editor)+2, len(editor)+2+m):
    a, *b = sys.stdin.readline().split()
    cursor = doWork((a, b), cursor, nord)

idx = 0
result = ''
while (llst[idx][2] != None):
    result += llst[idx][1]
    idx = llst[idx][2]

print(result)
print(llst)































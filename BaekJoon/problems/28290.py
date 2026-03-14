# 28290

import sys

ty = {'fdsajkl;':'in-out', 'jkl;fdsa':'in-out', 'asdf;lkj':'out-in', ';lkjasdf':'out-in', 'asdfjkl;':'stairs', ';lkjfdsa':'reverse'}

ipt = sys.stdin.readline().rstrip()

if (ipt in ty.keys()):
    print(ty[ipt])
else:
    print('molu')

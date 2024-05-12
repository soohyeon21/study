# 10600

import sys

color_idx = {1:(255, 255, 255), 2:(192, 192, 192), 3:(128, 128, 128), 4:(0, 0, 0),
             5:(255, 0, 0), 6:(128, 0, 0), 7:(255, 255, 0), 8:(128, 128, 0),
             9:(0, 255, 0), 10:(0, 128, 0), 11:(0, 255, 255), 12:(0, 128, 128),
             13:(0, 0, 255), 14:(0, 0, 128), 15:(255, 0, 255), 16:(128, 0, 128)}
color = {1:"White", 2:"Silver", 3:"Gray", 4:"Black", 5:"Red", 6:"Maroon",
         7:"Yellow", 8:"Olive", 9:"Lime", 10:"Green", 11:"Aqua", 12:"Teal",
         13:"Blue", 14:"Navy", 15:"Fuchsia", 16:"Purple"}

while (1):
    r, g, b = map(int, sys.stdin.readline().split())
    if (r == -1):
        break

    dist = []
    for i in range(1, 17):
        Ri, Gi, Bi = color_idx[i][0], color_idx[i][1], color_idx[i][2]
        d = ((Ri-r)**2 + (Gi-g)**2 + (Bi-b)**2)**0.5
        dist.append((d, i))
    dist.sort()
    print(color[dist[0][1]])

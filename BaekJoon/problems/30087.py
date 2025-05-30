# 30087

import sys

n = int(sys.stdin.readline())

classroom = {'Algorithm':204, 'DataAnalysis':207, 'ArtificialIntelligence':302, 'CyberSecurity':'B101', 'Network':303, 'Startup':501, 'TestStrategy':105}
for _ in range(n):
    seminar = sys.stdin.readline().rstrip()
    print(classroom[seminar])

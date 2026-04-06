# Yangjojang of The Year

import sys

n = int(sys.stdin.readline())

matrix = {}

for i in range(n):
    m = int(sys.stdin.readline())
    for j in range(m):
        a,b = sys.stdin.readline().split()
        matrix[a] = int(b)

    res = max(matrix.values())
    tmp = {v: k for k, v in matrix.items()}
    print(tmp[res])
    matrix = {}
    tmp = {}
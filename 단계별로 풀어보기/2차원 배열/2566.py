# 최댓값 !!
import numpy as np
matrix = []

for i in range(9):
    a = list(map(int,input().split()))
    matrix.append(a)

max = matrix[0][0]
max_i, max_j = 0,0

for i in range(9):
    for j in range(9):
        if max <= matrix[i][j]:
            max_i = i+1
            max_j = j+1
            max = matrix[i][j]
print(max)
print(max_i,max_j)

# max_val = max(map(max,matrix))
# print(max_val) # 2차원 배열에서 최대값 & 최소값 & 합 구하기
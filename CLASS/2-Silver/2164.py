# 카드2
from collections import deque
n = int(input())
matrix = deque(range(1,n+1))

while len(matrix) > 1:
  matrix.popleft()
  matrix.append(matrix[0])
  matrix.popleft()

print(matrix[0])

# 2164 번 - 큐를 사용하며, 빼고, 넣고, 빼고를 한 사이클 돌리기
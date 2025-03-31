# 덩치
n=int(input())
matrix = []

for _ in range(n):
  w,h = map(int, input().split())
  matrix.append((w,h))

for i in matrix:
  cnt = 1
  for j in matrix:
    if i[0] < j[0] and i[1] < j[1]:
      cnt += 1

  print(cnt, end=" ")

  # 7568 번
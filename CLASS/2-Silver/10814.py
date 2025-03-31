# 나이순 정렬
n=int(input())
matrix = []

for _ in range(n):
  age,name = input().split()
  matrix.append([int(age),name])

for i in sorted(matrix, key=lambda x : x[0]):
  print(i[0],i[1])

# 10814 번
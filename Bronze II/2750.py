# 수 정렬하기
n = int(input())
matrix = []

for i in range(n):
    matrix.append(int(input()))

matrix.sort()

for i in matrix:
    print(i)

# int(input())과 input() 차이는..?
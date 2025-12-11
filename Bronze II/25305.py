# 커트라인
n,k = map(int,input().split())
matrix = list(map(int,input().split()))

matrix.sort()
matrix.reverse()

print(matrix[k-1])
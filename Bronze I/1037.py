# 약수
# n => 1과 8 제외하고 약수의 개수
# 4 2 => 8의 약수는 1 2 4 8이기 때문에 4 랑 2만

n = int(input())
matrix = list(map(int,input().split()))

matrix.sort()

res = matrix[0]*matrix[len(matrix)-1]

print(res)
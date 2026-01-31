# 막대기
n = int(input())
matrix = []
cnt = 1

for i in range(n):
    matrix.append(int(input()))

for i in range(n-2,-1,-1):
    if matrix[n-1] < matrix[i]:
        cnt+=1

print(cnt)
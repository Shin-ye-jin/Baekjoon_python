# 그릇
matrix = list(input())
cnt = 10

for i in range(1,len(matrix)):
    if matrix[i] == matrix[i-1]:
        cnt+=5
    else:
        cnt+=10

print(cnt)
# 홀수
matrix=[]
for i in range(7):
    n = int(input())
    if n%2==1:
        matrix.append(n)

if len(matrix) == 0:
    print(-1)
else:
    print(sum(matrix))
    print(min(matrix))
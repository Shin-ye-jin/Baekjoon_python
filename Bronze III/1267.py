# 핸드폰 요금
n = int(input())
matrix = list(map(int,input().split()))
Y, M = 0,0

for i in range(n):
    Y += (matrix[i]//30 + 1)*10
    M += (matrix[i]//60 + 1)*15

if Y < M:
    print('Y',Y)
elif Y > M:
    print('M',M)
else:
    print('Y','M',Y)
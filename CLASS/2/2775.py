# 부녀회장이 될테야
matrix = [[0]*15 for i in range(15)]
cnt,sum=1,0

for i in range(15):
    matrix[0][i] = cnt
    cnt+=1

for i in range(1,15):
    for j in range(15):
        for z in range(j+1):
            sum += matrix[i-1][z]
        matrix[i][j]=sum
        sum=0

n=int(input())
for i in range(n):
    k=int(input())
    m=int(input())
    print(matrix[k][m-1])

# 1 층 3호 (0층의 1호부터 3호 - 1 + 2 + 3)
# 2 층 3호 (1층의 1호부터 3호 - 1 + (1+2) + (1+2+3))
# 지능형 기차
matrix=[]
cnt = 0

for i in range(4):
    a,b=map(int,input().split())
    cnt = cnt - a + b
    matrix.append(cnt)

print(max(matrix))
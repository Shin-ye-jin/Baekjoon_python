# 공 넣기
n,m=map(int,input().split())
num=[0]*n

for i in range(m):
    i,j,k=map(int,input().split())
    for a in range(i-1,j):
        num[a]=k

for i in num:
    print(i,end=' ')
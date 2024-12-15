# 공 바꾸기
n,m=map(int,input().split())
num=[0]*n
tmp=0

for i in range(n):
    num[i]=i+1

for i in range(m):
    i,j=map(int,input().split())
    tmp = num[i-1]
    num[i-1]=num[j-1]
    num[j-1]=tmp

for i in num:
    print(i,end=' ')
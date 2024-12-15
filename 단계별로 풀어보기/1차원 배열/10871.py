# X보다 작은 수
n,x=map(int,input().split())
num=list(map(int,input().split()))

for i in num:
    if i<x:
        print(i,end=" ")
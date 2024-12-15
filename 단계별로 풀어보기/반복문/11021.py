# A+B -7
n = int(input())

for i in range(n):
    a,b=map(int,input().split())
    print("Case #%d:"%(i+1),end=' ')
    print(a+b)
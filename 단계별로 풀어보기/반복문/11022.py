# A+B -8
n=int(input())

for i in range(n):
    a,b=map(int,input().split())
    print("Case #%d: %d + %d = "%(i+1,a,b),end='')
    print(a+b)
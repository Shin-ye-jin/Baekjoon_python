# 최대공약수와 최소공배수

n,m=map(int,input().split())
l = min(n,m)
for i in range(l,0,-1):
    if n%i==0 and m%i==0:
        print(i)
        print(i*(n//i)*(m//i))
        break
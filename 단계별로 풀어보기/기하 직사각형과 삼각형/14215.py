# 세 막대
a,b,c=map(int,input().split())
sum=a+b+c
m=max(a,b,c)

if m < sum-m:
    print(a+b+c)
else:
    m2 = sum-m-1
    print(m2+sum-m)


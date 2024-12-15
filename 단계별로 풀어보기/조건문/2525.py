# 오븐 시계
a,b=map(int,input().split())
c=int(input())

h = c//60
m = c%60

a +=h
b +=m

if a>23:
    a-=24
    if b>=60:
        b-=60
        a+=1
        print(a,b)
    else:
        print(a,b)
else:
    if b>=60:
        b-=60
        a+=1
        if a>23:
            a-=24
            print(a,b)
        else:
            print(a,b)
    else:
        print(a,b)
# 소인수분해
n=int(input())
m=2

while True:
    if n%m==0:
        print(m)
        n//=m
    else:
        m+=1

    if n==1:
        break
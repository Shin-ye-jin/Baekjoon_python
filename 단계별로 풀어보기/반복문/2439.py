# 별 찍기-2
n=int(input())

for i in range(1,n+1):
    for j in range(n-1,i-1,-1):
        print(" ",end='')
    for j in range(i):
        print("*",end='')
    print()

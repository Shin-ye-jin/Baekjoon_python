# 별 찍기 - 9
n = int(input())

for i in range(n,0,-1):
    for j in range(n,i,-1):
        print(" ",end='')

    for j in range(2*i-1,0,-1):
        print("*",end='')

    print()

for i in range(2,n+1):
    for j in range(n,i,-1):
        print(" ",end='')

    for j in range(i*2-1):
        print("*",end='')

    print()
# 별 찍기 - 8
n= int(input())

for i in range(1,n+1):
    for j in range(i):
        print("*",end='')
    for j in range(n*2,i*2,-1):
        print(" ",end='')
    for j in range(i):
        print("*",end='')
    print()

for i in range(n-1,0,-1):
    for j in range(i,0,-1):
        print("*",end='')
    for j in range(0,(n-i)*2):
        print(" ",end='')
    for j in range(i,0,-1):
        print("*",end='')
    print()
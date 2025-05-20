# 별 찍기 - 5
n = int(input())

for i in range(0,n):
    for j in range(n,i+1,-1):
        print(" ",end="")

    for j in range(0,i*2+1):
        print("*",end='')
    print()
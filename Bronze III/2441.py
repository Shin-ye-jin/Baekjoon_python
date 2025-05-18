# 별 찍기 - 4
n = int(input())

for i in range(n):
    for j in range(0,i):
        print(" ",end='')

    for j in range(i,n):
        print("*",end='')
    print()
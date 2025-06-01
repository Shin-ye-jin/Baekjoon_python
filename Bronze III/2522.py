# 별 찍기 - 12
n = int(input())

for i in range(1,n+1):
    for j in range(i,n):
        print(" ",end='')
    for j in range(i):
        print("*",end='')
    print()

for i in range(1,n):
    for j in range(i):
        print(" ",end='')
    for j in range(i,n):
        print("*",end='')
    print()
# 별 찍기 - 6
n = int(input())

for i in range(n):
    for j in range(i):
        print(" ",end='')

    for j in range((n-i)*2,1,-1):
        print("*",end='')

    print()
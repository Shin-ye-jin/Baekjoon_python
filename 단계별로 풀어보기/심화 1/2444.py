# 별 찍기 -7
n=int(input())

for i in range(1,n+1):
    for j in range(i,n):
        print(" ",end='')
    for j in range(1,2*i):
        print("*",end='')
    print()
for i in range(1,n):
    for j in range(i):
        print(" ",end='')
    for j in range(2*n-1,i*2,-1):
        print("*",end='')
    print()
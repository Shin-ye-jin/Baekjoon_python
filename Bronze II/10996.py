# 별 찍기 - 21
n = int(input())

for z in range(n):
    for i in range(n):
        if i%2==0:
            print('*',end='')
        else:
            print(' ',end='')

    print()

    for j in range(n):
        if j%2==1:
            print('*',end='')
        else:
            print(' ',end='')
    print()
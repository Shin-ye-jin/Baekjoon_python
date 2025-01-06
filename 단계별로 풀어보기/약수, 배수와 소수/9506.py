# 약수들의 합
while True:
    res = 0
    result = []

    n=int(input())

    if n == -1: break

    for i in range(1,n):
        if n%i==0:
            res += i
            result.append(i)

    if res == n:
        print(n,"= ",end='')
        for i in range(len(result)-1):
            print(result[i],end=' + ')
        print(result[i+1])
    else:
        print(n,"is NOT perfect.")


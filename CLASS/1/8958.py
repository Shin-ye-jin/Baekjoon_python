# OX 퀴즈
n=int(input())
cnt,sum=0,0
for i in range(n):
    matrix = list(input())
    for j in range(len(matrix)):
        if matrix[j] == "O":
            cnt+=1
            sum+=cnt
        else:
            cnt=0
    print(sum)
    cnt,sum=0,0
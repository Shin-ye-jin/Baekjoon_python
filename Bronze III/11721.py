# 열 개씩 끊어 출력하기
matrix = list(input())

for i in range(len(matrix)):
    print(matrix[i],end='')
    if (i+1)%10==0:
        print()
# 세로 읽기
matrix = []

for i in range(5):
    a = input()
    matrix.append(a)

for j in range(15):
    for i in range(5):
        if j < len(matrix[i]):
            print(matrix[i][j],end='')

# 배열 역순으로 출력하기
# 2차원 배열로서 하나씩 입력 받기?
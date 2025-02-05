# 직각삼각형
while True:
    matrix = list(map(int,input().split()))
    if matrix[0]==0 and matrix[1]==0 and matrix[2]==0:
        break
    matrix.sort()
    if matrix[0]**2 + matrix[1]**2 == matrix[2]**2:
        print("right")
    else:
        print("wrong")

# 리스트를 사용하라!
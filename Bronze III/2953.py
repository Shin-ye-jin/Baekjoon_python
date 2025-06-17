# 나는 요리사다
matrix = []

for i in range(5):
    a,b,c,d = map(int,input().split())
    matrix.append(a+b+c+d)

print(matrix.index(max(matrix))+1,max(matrix))
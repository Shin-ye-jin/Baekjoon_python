# 대표값2
matrix=[]
for i in range(5):
    matrix.append(int(input()))

avg = sum(matrix)//5
matrix.sort()
print(avg)
print(matrix[2])
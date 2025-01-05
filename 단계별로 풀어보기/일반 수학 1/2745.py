# 진법 변환
matrix=[chr(i) for i in range(ord('A'),ord('Z')+1)]
n,m = input().split()

matrix2 = list(n)
m=int(m)

cnt, result = 1, 0
for i in range(len(matrix2)-1,-1,-1):
    if ord(matrix2[i]) >= 65:
        result = result + (matrix.index(matrix2[i])+10)*cnt
    else:
        result = result + int(matrix2[i])*cnt
    cnt*=m
print(result)
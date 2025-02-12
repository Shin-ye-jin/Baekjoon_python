# 블랙잭 !! 더욱더 하기
n,m = map(int,input().split())
matrix = list(map(int,input().split()))
res = 0

for i in range(n):
    for j in range(i+1,n):
        for z in range(j+1,n):
            if matrix[i] + matrix[j] + matrix[z] > m:
                continue
            else:
                res = max(res, matrix[i] + matrix[j] + matrix[z])

print(res)
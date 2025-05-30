# 전자레인지
matrix =[300,60,10]
res=[]
n = int(input())

for i in range(3):
    res.append(str(n//matrix[i]))
    n = n%matrix[i]

if n==0:
    print(" ".join(res))
else:
    print(-1)
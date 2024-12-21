# 킹, 퀸, 룩, 비숍, 나이트, 폰
num = [1,1,2,2,2,8]
matrix=list(map(int,input().split()))

for i in range(len(num)):
    print(num[i]-matrix[i],end=' ')
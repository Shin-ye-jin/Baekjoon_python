# 소수 찾기
n=int(input())
cnt,cnt2=1,0

num = list(map(int,input().split()))
matrix = []

for i in range(n):
    for j in range(2,num[i]):
        if num[i]%j==0:
            cnt+=1
    if num[i]==1:
        matrix.append(0)
    else:
        matrix.append(cnt)

    cnt=1

for i in range(n):
    if matrix[i] == 1:
        cnt2+=1

print(cnt2)
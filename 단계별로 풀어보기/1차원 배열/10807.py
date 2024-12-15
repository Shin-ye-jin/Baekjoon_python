# 개수 세기
n=int(input())
num=list(map(int,input().split()))
v=int(input())
cnt=0

for i in num:
    if v==i:
        cnt+=1

print(cnt)
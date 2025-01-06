# 소수
n=int(input())
m=int(input())

res=[]
cnt,cnt2=0,0

if n==1: n+=1

for i in range(n,m+1):
    for j in range(2,i):
        if i%j==0:
            cnt+=1

    if cnt==0:
        res.append(i)
        cnt2+=i
    cnt=0

if cnt2 != 0:
    print(cnt2)
    print(res[0])
else:
    print(-1)
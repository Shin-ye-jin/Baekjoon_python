# 소수
n=int(input())
m=int(input())

res=[]

for i in range(n,m+1):
    cnt=0
    if i>1:
        for j in range(2,i):
            if i%j==0:
                cnt+=1
                break

        if cnt==0:
            res.append(i)

if len(res) < 1:
    print(-1)
else:
    print(sum(res))
    print(min(res))
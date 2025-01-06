# 약수 구하기
n,k=map(int,input().split())
cnt=[]

for i in range(1,n+1):
    if n%i==0:
        cnt.append(i)

if len(cnt) >= k:
    print(cnt[k-1])
else:
    print(0)
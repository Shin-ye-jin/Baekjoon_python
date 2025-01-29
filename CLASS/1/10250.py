# ACM 호텔
t=int(input())
cnt,a,b=0,0,0
for i in range(t):
    h,m,n=map(int,input().split())
    for j in range(1,m+1):
        for z in range(1,h+1):
            cnt+=1
            if cnt==n:
                if j<10:
                    j = format(j,'02')
                    print(str(z)+str(j))
                else:
                    print(str(z)+str(j))
    cnt=0
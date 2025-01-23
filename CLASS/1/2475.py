# 검증수
num=list(map(int,input().split()))
sum=0

for i in range(len(num)):
    sum+=num[i]*num[i]

print(sum%10)
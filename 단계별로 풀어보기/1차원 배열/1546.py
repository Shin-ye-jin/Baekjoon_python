# 평균
n=int(input())
num=list(map(int,input().split()))
m, sum = max(num),0
for i in range(n):
    num[i] = num[i]/m*100
    sum+=num[i]

print(sum/n)
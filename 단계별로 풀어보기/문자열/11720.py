# 숫자의 합
n=int(input())
m=int(input())
sum=0

for i in range(n):
    sum+=m%10
    m//=10

print(sum)

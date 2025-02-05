# 분해합
n=int(input())
sum=0

for i in range(1,n+1):
    m=list(str(i))
    sum+=i

    for j in range(len(m)):
        sum+=int(m[j])

    if sum==n:
        print(i)
        break
    sum=0

    if i==n:  # 문제 제대로 읽기...
        print(0)
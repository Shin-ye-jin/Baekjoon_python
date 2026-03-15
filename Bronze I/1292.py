# 쉽게 푸는 문제

a,b = map(int,input().split())
cnt = 0

n = 0

res = 0

while True:
    n +=1
    for i in range(1,n+1):
        cnt+=1
        if a<=cnt<=b:
            res += n
    if cnt > b:
        break

print(res)
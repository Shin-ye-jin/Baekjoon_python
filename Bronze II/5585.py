# 거스름돈
cnt = [500,100,50,10,5,1]
res = []
n = int(input())

tmp = 1000 - n

for i in range(len(cnt)):
    num = tmp//cnt[i]
    res.append(num)
    tmp%=cnt[i]

print(sum(res))

# 메모이제이션을 사용한 것이 맞나? 뭐 쨋든 비슷하게 해봄!

# 세탁소 사장 동혁
cnt = [25,10,5,1]

n = int(input())

for i in range(n):
    m=int(input())
    for j in range(4):
        print(m//cnt[j],end=' ')
        m%=cnt[j]
    print()

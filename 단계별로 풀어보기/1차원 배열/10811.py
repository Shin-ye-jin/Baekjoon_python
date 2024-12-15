# 바구니 뒤집기
n,m=map(int,input().split())
num=[i for i in range(1,n+1)]
tmp = 0

for a in range(m):
    i,j=map(int,input().split())
    tmp = num[i-1:j]
    tmp.reverse()
    num[i-1:j]=tmp

for i in num:
    print(i,end=' ')

# 반복 횟수 만큼 i,j를 입력받기
# 슬라이싱하여 역순으로 만들어주고 업데이트하기 !!
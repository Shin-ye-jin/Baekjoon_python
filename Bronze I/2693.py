# N번째 큰 수

n = int(input())
m=[]

for i in range(n):
    m = list(map(int,input().split()))
    m.sort()
    print(m[-3])
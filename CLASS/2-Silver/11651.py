# 좌표 정렬하기 2
n=int(input())
res=[]

for i in range(n):
  x,y=map(int,input().split())
  res.append([x,y])

res.sort(key = lambda x : (x[1],x[0]))

for i in res:
  print(i[0],i[1])

# 11651번
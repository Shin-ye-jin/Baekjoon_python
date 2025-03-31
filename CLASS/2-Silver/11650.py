# 좌표 정렬하기
n=int(input())
res = []

for i in range(n):
  x,y=map(int,input().split())
  res.append([x,y])

res.sort()

for i in range(n):
  print(res[i][0],res[i][1])
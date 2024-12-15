# 최댓값
num=[0]*9
max,cnt=0,0
for i in range(9):
    num[i]=int(input())
    if max < num[i]:
        max=num[i]
        cnt=i

print(max)
print(cnt+1)
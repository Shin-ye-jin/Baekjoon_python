# 과제 안 내시 분...?
num=[0]*30

for i in range(28):
    n=int(input())
    num[n-1]=1

for i in range(30):
    if num[i]==0:
        print(i+1)
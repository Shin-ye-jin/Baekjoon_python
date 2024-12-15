a=int(input())
b=int(input())
num=[]
for i in str(b):
    num.append(i)
for i in range(2,-1,-1):
    print(a*int(num[i]))
print(a*b)
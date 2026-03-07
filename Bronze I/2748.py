# 피보나치 수 2
n = int(input())
a = 0
b = 1
c = 1

for i in range(1,n):
    c = a+b
    a = b
    b = c

print(c)
# 별 찍기 - 13
# n = int(input())
#
# for i in range(1,n+1):
#     for j in range(i):
#         print("*",end='')
#
#     for j in range(i,n):
#         print(" ",end='')
#     print()
#
# for i in range(n-1):
#     for j in range(n-1,i,-1):
#         print("*",end='')
#
#     for j in range(i,n):
#         print(" ",end='')
#     print()

n = int(input())

for i in range(1,n):
    print("*"*i)
for i in range(n,0,-1):
    print("*"*i)
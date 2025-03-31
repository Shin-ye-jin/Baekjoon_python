# 팩토리얼 0의 개수

def f(n):
    if n<1:
        return 1
    else:
        return n*f(n-1)

n=int(input())
cnt=0
num = f(n)
matrix = list(str(num))

for i in range(len(matrix)-1,0,-1):
    if matrix[i]=='0':
        cnt+=1
    else:
        break

print(cnt)
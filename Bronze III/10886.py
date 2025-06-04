# 0 = not cute / 1 = cute
matrix = []
n = int(input())

for i in range(n):
    matrix.append(int(input()))

if matrix.count(0) > matrix.count(1):
    print("Junhee is not cute!")
else:
    print("Junhee is cute!")
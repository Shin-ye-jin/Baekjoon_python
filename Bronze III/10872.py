# 팩토리얼
def f(n):
    if n<1:
        return 1
    else:
        return n*f(n-1)

n = int(input())
print(f(n))
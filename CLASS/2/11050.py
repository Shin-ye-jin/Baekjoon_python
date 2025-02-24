# 이항 계수 1
def f(n):
    if n<=1:
        return 1
    else:
        return n*f(n-1)

n,k=map(int,input().split())
res = f(n)/(f(n-k)*f(k))
print(int(res))

# 이항 계수 nCk = n! / (n-k)! * k!

# 피보나치 수 5

# n = int(input())
# a,b,c = 0,1,0
#
# for i in range(1,n):
#     c = a+b
#     a = b
#     b = c
#
# print(c)
# 답은 나오는데 이유는 모르나 틀림...

# 피보나치 수열 재귀함수 사용하기
def f(n):
    if n<=1:
        return n
    return f(n-1) + f(n-2)

n = int(input())
print(f(n))
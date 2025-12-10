# 피보나치 수
# def f(n):
#     if n<=2:
#         return 1
#     else:
#         return f(n-1)+f(n-2)
#
# n = int(input())
# print(f(n))

# 아니... 답은 맞는데 시간 초과래 이게 맞냐
# 메모이제이션 기법 사용하기

def f(n):
    tmp = [0,1]
    for i in range(2,n+1):
        tmp.append(tmp[i-1]+tmp[i-2])
    return tmp[n]

num = int(input())
print(f(num))
# 8진수 2진수

n = input()
res = int(n,8)
tmp = bin(res)

print(tmp[2:])

# [2:]으로 하여 2번재 자리부터 출력될 수 있도록 한다.
# Hashing
# n=int(input())
# matrix = list(input())
#
# m = [chr(i) for i in range(ord('a'),ord('z')+1)]
#
# cnt = 1
# res = 0
# for i in range(len(matrix)):
#     res = res + (m.index(matrix[i])+1) * cnt
#     cnt*=31
#
# print(res)

# 위의 것은 부분정답 인정
# 하단부가 정답!

n = int(input())
s = list(input())
res = 0

for i in range(n):
    res += ((ord(s[i])- 96) * (31**i)) # 소문자 a가 97이다!

print(res % 1234567891)
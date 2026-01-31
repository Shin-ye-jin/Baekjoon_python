# 뒤집힌 덧셈
# 역순으로 바꾸는 가장 간단한 방법
# 숫자를 문자열로 바꾸고, 문자열 슬라이싱을 이용해 뒤집고 다시 정수로 변환
# [::-1] : 문자열을 뒤집는 파이썬 슬라이싱 문법

a,b = map(int,input().split())

re_as = str(a)[::-1]
re_bs = str(b)[::-1]

re_a = int(re_as)
re_b = int(re_bs)

num = re_a + re_b
re_nums = str(num)[::-1]
print(int(re_nums))
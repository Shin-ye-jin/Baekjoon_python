# 숫자의 개수 !!
a=int(input())
b=int(input())
c=int(input())

num = a*b*c
num = str(num)

for i in range(10):
    n_count = num.count(str(i))
    print(n_count)

# 숫자를 list로 변환 n = list(map(int,str(num)))
# count 함수는 문자열 내부에서 특정 문자, 혹은 문자열이 포함되어 있는지 계산
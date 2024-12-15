# 나머지
num=[0]*10
result=[]
for i in range(10):
    n=int(input())
    num[i] = n%42

for value in num: # 리스트 내 중복 제거
    if value not in result:
        result.append(value)

print(len(result))
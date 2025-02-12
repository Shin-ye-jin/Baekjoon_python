# 벌집 !! 더욱더 하기
n=int(input())

cnt = 1 # 벌집의 개수
res = 1 # 결과

while n > cnt:
    cnt += 6*res
    res += 1

print(res)

# 벌집의 개수가 6의 배수를 증가하고 있다.
# 규칙성 있게 한 겹씩 쌓이고 있는 것이다.!!
# 몇 번째 껍질에 있느냐!
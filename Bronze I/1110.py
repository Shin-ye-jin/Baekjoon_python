# 더하기 사이클
# 26 => 2+6=8
# 68 => 6+8=14 (6+8)
# 84 => 8+4=12 (8+4)
# 42 => 4+2=6 (4+2)
# 새로운 수 26 (2+6)

a = int(input())

res = a
cnt = 0
while True:
    x = a//10
    y = a%10
    z = (x + y)%10

    a = y*10 + z
    cnt += 1
    if a == res:
        break

print(cnt)
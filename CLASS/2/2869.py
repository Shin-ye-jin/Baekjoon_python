# 달팽이는 올라가고 싶다
# a,b,v = map(int,input().split())
# sum,cnt=0,0
#
# while True:
#     sum+=a
#     cnt += 1
#     if sum>=v: break
#     sum-=b
#     if sum>=v: break
#
# print(cnt)

# 시간 초과 ㅠㅠ....

# 낮 2 밤 -1 높이 5
# 2-1 2-1 2-1 2 !! 도착 -> 4일 걸림
# 낮 5 밤 -1 높이 6
# 5-1 5 !! 도착 -> 2일 걸림


a,b,v=map(int,input().split())

if (v-b) % (a-b) == 0:
    print((v-b)//(a-b))
else:
    print((v-b)//(a-b)+1)

# 올라가야할 거리 = v-b .... 왜냐 미끄러지기 전에 도달하면 된다인가?
# 하루에 갈 수 있는 거리 = a-b
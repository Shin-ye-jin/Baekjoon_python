# 수 정렬하기 3
# matrix = []
# n=int(input())
#
# for i in range(n):
#     m=int(input())
#     matrix.append(m)
#
# matrix.sort()
#
# for i in range(n):
#     print(matrix[i])

# 시간 초과

# 계수 정렬 사용
import sys
input = sys.stdin.readline

n=int(input())
arr = [0]*(10000+1)

for _ in range(n):
    arr[int(input())] += 1
# (2) 1 1 1 3 2 1을 입력 받았다면 arr[0,4,1,1]

for i in range(len(arr)):
    if arr[i] != 0:
        for _ in range(arr[i]): # arr[1]이 4라면 1을 4번 출력!!
            print(i)
# 줄 세우기
# 첫 번째로 줄 선 학생 무조건 0번 제일 앞
# 두 번째로 줄 선 학생 0 or 1번
# 0번을 봅으면 그 자리에 있음
# 1번 봅으면 바로 앞의 학생 앞으로 감
# 세 번재로 줄 선 학생은 0, 1, 2

# n = int(input())
# matrix = list(input().split())
# result = []
#
# for i in range(n):
#     if matrix[i] == '0':
#         result.append(i+1)
#     elif matrix[i] == '1':
#         result.insert(i-1,i+1)
#     elif matrix[i] == '2':
#         result.insert(i-2,i+1)
#     elif matrix[i] == '3':
#         result.insert(i-3,i+1)
#
# print(result)

n = int(input())
matrix = list(map(int,input().split()))
result = []

for i in range(n):
    if matrix[i] == 0:
        result.insert(0,i+1)
    else:
        result.insert(matrix[i],i+1)

for i in reversed(result):
    print(i,end=' ')

# 이런건가? 오름차순으로 했다가 내림차순으로 변경?
# ... 와우
# 오큰수
# 오른쪽에 있으면서 Ai보다 큰 수 중! 가장 왼쪽에 있는 수
# 오른쪽 있는 것들을 리스트로 뽑아온다?
# 그리고 크기 비교를 해서 가장 큰 것을 출력한다?
# 없으면 -1?

import sys
n = int(sys.stdin.readline())
matrix = list(map(int,sys.stdin.readline().split()))
answer = [-1]*n
res = [0]

for i in range(1,n):
    while res and matrix[res[-1]] < matrix[i]:
        answer[res.pop()] = matrix[i]
    res.append(i)

print(*answer)

# res라는 리스트를 만들어서 인덱스를 저장하도록 하기
# answer라는 리스트를 만들어서 결과를 저장하기
# 반복문을 돌려서 res 리스트에서 인덱스를 가져와 비교
# 맞으면 res 리스트에서 인덱스를 뽑아와 없애기
# answer 리스트 해당 인덱스에 오큰수를 집어넣기
# 끝났으면 다음 인덱스 값을 res 리스트에 넣기

# for i in range(n):
#     num = matrix[i]
#     for j in range(i+1,n):
#         if num < matrix[j]:
#             cnt+=1
#             print(matrix[j],end=' ')
#             break
#
#     if cnt == 0:
#         print(-1,end=' ')
#     cnt=0
# 성공은 했으나 시간 초과

# for i in range(n):
#     num = matrix[i]
#     matrix2 = matrix[start:end]
#     for j in range(len(matrix2)):
#         tmp = matrix2.pop(0)
#         #print(tmp)
#         if num < tmp:
#             cnt+=1
#             print(tmp,end=' ')
#             break
#
#     if cnt == 0:
#         print(-1,end=' ')
#     cnt=0
#     start += 1
# 성공은 했으나 시간 초과


# for i in range(n):
#     num = matrix[i]
#     matrix2 = matrix[start:end]
#
#     if len(matrix2)==0:
#         print(-1)
#         break
#
#     if num < max(matrix2):
#         print(max(matrix2),end=' ')
#     else:
#         print(-1,end=' ')
#
#     start += 1
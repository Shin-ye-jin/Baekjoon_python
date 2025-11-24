# 오큰수
# 오른쪽에 있으면서 Ai보다 큰 수 중! 가장 왼쪽에 있는 수
# 오른쪽 있는 것들을 리스트로 뽑아온다?
# 그리고 크기 비교를 해서 가장 큰 것을 출력한다?
# 없으면 -1?

n = int(input())
matrix = list(map(int,input().split()))

print(matrix)
print(max(matrix[1:]))
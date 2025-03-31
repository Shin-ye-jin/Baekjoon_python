# 단어 정렬 < 실버 >
import sys

n=int(input())
matrix=[]

for i in range(n):
    m=sys.stdin.readline().strip()
    matrix.append(m)

matrix = set(matrix) # 중복값 제거
matrix = list(matrix) # 리스트로 변환

matrix.sort()
matrix.sort(key = len) # 문자열 길이 순으로 정렬

for i in matrix:
    print(i)

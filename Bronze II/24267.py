# 알고리즘 수업 - 알고리즘의 수행 시간 6
# 전체 수행 횟수는 1부터 n-2까지 각 1부터 해당 값까지의 합의 결과를 모두 더한 결과

# 시그마 k(k+1)/2 이고 이것을 풀어서 정리하면 n(n-1)(n-2)/6 으로 나타낼 수 있다.
n=int(input())

result=0

for i in range(1,n-1):
    for j in range(i+1, n):
        for k in range(j+1,n+1):
            result+=1

print(int((n*(n-1)*(n-2))/6))
print(3)
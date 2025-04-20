# 18110 solved.ac
# import sys

# def mround(val):
#   if val - int(val) >= 0.5:
#     return int(val)+1
#   else:
#     return int(val)

# n = int(sys.stdin.readline().strip())

# if n:
#   level = []
#   for _ in range(n): # n==0이 아니라면 모든 난이도 의견을 level 리스트에 저장하고 오름차순 정렬
#     level.append(int(sys.stdin.readline().strip()))

#   m=mround(n*0.15) # 절사평균 15%를 구한다. 10명이면 2명!
#   level.sort()

#   if m>0: # 가장 높은 난이도에 투표한 m명과 가장 낮은 난이도에 투표한 m명의 난이도 의견 제외하고 나머지 난이도 의견들의 평균 구함
#     print(mround(sum(level[m:-m])/len(level[m:-m])))
#   else:
#     print(mround(sum(level)/len(level)))
# else: # n==0 이라면 아직 아무의견이 없는 것으로 0을 출력한다.
#   print(0)



# 18110번
# 오사오입으로 처리한다. - 5 미만의 숫자는 내림, 5 초과의 숫자는 올림
# 만약 반올림할 자릿수가 5일 경우 5의 앞자리가 홀수 인 경우 올림, 짝수인 경우 내림
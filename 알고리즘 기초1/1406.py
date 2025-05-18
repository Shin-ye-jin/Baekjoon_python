# 에디터
# matrix = list(input())
# n=int(input())
#
# num=len(matrix)
#
# for i in range(n):
#     m = list(input().split())
#
#     if m[0] == 'P':
#         matrix.insert(num,m[1])
#         num += 1
#     elif m[0] == 'L':
#         if num > 0:
#             num -= 1
#     elif m[0] == 'D':
#         if num < len(matrix):
#             num += 1
#     elif m[0] == 'B':
#         if num > 0:
#             del matrix[num-1]
#             num -= 1
#
# for i in range(len(matrix)):
#     print(matrix[i],end="")
# 돌아는 가나! 시간복잡도 문제로 시간 초과!!

# import sys
# input = sys.stdin.readline
#
# s1 = list(input().rstrip())
# s2 = []
# for _ in range(int(input())):
#     cmd = input().split()
#     if cmd[0] == "L":
#         if s1:
#             s2.append(s1.pop())
#     elif cmd[0] == "D":
#         if s2:
#             s1.append(s2.pop())
#     elif cmd[0] == "B":
#         if s1:
#             s1.pop()
#     else:
#         s1.append(cmd[1])
# s1.extend(reversed(s2))
# print("".join(s1))

import sys

m_l = list(sys.stdin.readline().rstrip())
m_r = []

n = int(input())

for i in range(n):
    c = sys.stdin.readline().split()

    if c[0] == 'L': # if 2가지로 나누니 정답..?
        if m_l:
            m_r.append(m_l.pop())
    elif c[0] == 'D':
        if m_r:
            m_l.append(m_r.pop())
    elif c[0] == 'B':
        if m_l:
            m_l.pop()
    else:
        m_l.append(c[1])

m_l.extend(reversed(m_r))
print(''.join(m_l))

# 최종 문제 풀이는 스택 2개를 사용하면서 if문 잘쓰자..

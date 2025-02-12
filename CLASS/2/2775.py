# 부녀회장이 될테야
matrix = [[0]*14 for i in range(14)]
cnt=1
for i in range(14):
    matrix[0][i] = cnt
    cnt+=1

# for i in range(1,14):
#    for j in range(14):


# 1 층 3호 (0층의 1호부터 3호 - 1 + 2 + 3)
# 2 층 3호 (1층의 1호부터 3호 - 1 + (1+2) + (1+2+3))
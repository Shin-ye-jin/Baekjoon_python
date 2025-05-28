# 윷놀이
for i in range(3):
    matrix = list(map(int,input().split()))

    if matrix.count(0) == 1:
        print("A")
    elif matrix.count(0) == 2:
        print("B")
    elif matrix.count(0) == 3:
        print("C")
    elif matrix.count(0) == 4:
        print("D")
    else:
        print("E")
    matrix.clear()
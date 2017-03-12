def getMaxOfRows(M,O,P):
    arr = [M,O,P]
    sum_m = sum(M)
    sum_o = sum(O)
    sum_p = sum(P)
    three_leaves = [sum_m,sum_o,sum_p]
    max_row_sum = max(three_leaves)
    i = 0
    column_sum = []
    for i in range(3):
        res = 0
        for j in range(3):
            res += arr[j][i]
        column_sum.append(res)
    max_column = max(column_sum)
    totalMax = max([max_row_sum, max_column])
    if totalMax!=0 and totalMax%2 == 0:
        return totalMax - 1
    return totalMax




T = int(input())
for _ in range(T):
    M = [int(temp) for temp in input().split(' ')]
    O = [int(temp) for temp in input().split(' ')]
    P = [int(temp) for temp in input().split(' ')]
    print(getMaxOfRows(M,O,P))

T = int(input())
for _ in range(T):
    n,m = input().split(' ')
    n,m = [int(n),int(m)]
    cost_n = [int(temp) for temp in input().split(' ')]
    arr_m = []
    arr_sum = []
    for _ in range(m):
        arr_m.append([int(temp) for temp in input().split(' ')])

    sum_n = sum(cost_n)
    i = 0
    min_val = -1
    total_sum = ((n *(n+1))//2)
    sums = [0]*total_sum
    sets = []*total_sum

    while i < m:
        j = 0
        res = 0
        distinct = set()
        for meal in arr_m[i][2:]:
            distinct.add(meal)
        res += arr_m[i][0]
        while j < m and distinct.__len__() != n:
            addedAtleastOne = False
            for meal in arr_m[j][2:]:
                if meal not in distinct:
                    addedAtleastOne = True
                    distinct.add(meal)
            if addedAtleastOne:
                res += arr_m[j][0]
            if distinct.__len__() == n:
                break
            j += 1
        if (min_val == -1 or min_val > res) and (res != 0 and distinct.__len__() == n):
            min_val = res
        i += 1
    if min_val != -1:
        print(min([sum_n, min_val]))
    else:
        print(sum_n)
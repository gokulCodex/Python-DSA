def combinationSort(strList):
    i, j = 0, 1
    while j < len(strList):
        while i < j:
            if strList[i][0] > strList[j][0]:
                strList[i], strList[j] = strList[j], strList[i]
            i += 1
        i = 0
        j += 1
    L1 = []
    for k in strList:
        L1.append(k)
    l, m = 0, 1
    while m < len(strList):
        while l < m:
            if strList[l][0] == strList[m][0]:
                lis1 = strList[l][1:]
                lis2 = strList[m][1:]
                if int(lis1) < int(lis2):
                    strList[l], strList[m] = strList[m], strList[l]
            l += 1
        l = 0
        m += 1
    return (L1, strList)
print(combinationSort(['d34', 'g54', 'd12', 'b87', 'g1', 'c65', 'g40', 'g5', 'd77']))
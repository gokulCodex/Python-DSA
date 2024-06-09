def selection_sort(L):
    i=0
    j=1
    while j<len(L):
        while i<j:
            if L[i]>L[j]:
                L[i],L[j]=L[j],L[i]
            i+=1
        i=0
        j+=1
    return L
print(selection_sort([5,2,3,7,5,9,12,11,3]))
    
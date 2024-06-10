def histogram(L):               #Function that returns a list of tuples containing the quantity and occurrences of that quantity,
    lis=[]                      #sorted in ascending order based on the number of occurrences. If occurrences are same, it is sorted
    L=sorted(L)                 #in ascending order based on the quantity
    count=0
    i,j=0,0
    while i<len(L):
        while j<len(L):
            if L[i]==L[j]:
                count+=1
                if j==len(L)-1:
                    lis.append((L[i],count))
                j+=1
            else:
                lis.append((L[i],count))
                break
        count=0
        i=j
    lis=sorted(lis,key=lambda x:(x[1],x[0]))
    return lis
L=[13,12,13,14,12,13,11,13,15,14,15]
print(histogram(L))
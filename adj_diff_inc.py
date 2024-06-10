def expanding(L):                     #Function that returns True if absolute diff bw each adjecent pair of L increases strictly
    if L==[]:
        return 'Nothing to show'      
    i=0
    count=0
    while i<len(L)-2:
        if abs(L[i+1]-L[i])<abs(L[i+2]-L[i+1]):
            count+=1
        i+=1
    return bool(count==len(L)-2)
print(expanding([1,2,3,4,5]))
def rev(L):
    if L==[]:
        return False
    left,right=0,len(L)-1
    while left<right:
        L[left],L[right]=L[right],L[left]
        left+=1
        right-=1
    return L
print(rev([1,2,3,4,5,6,7,8,9,10]))
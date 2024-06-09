def rev(s):
    L=[]
    for i in s:
        L.append(i)
    if L==[]:
        return False
    left,right=0,len(L)-1
    while left<right:
        L[left],L[right]=L[right],L[left]
        left+=1
        right-=1
    str=L[0]
    for j in range(1,len(L)):
        str=str+L[j]
    return str

print(rev('gokulCodex'))
def odd_one(L):
    i=0
    l=type(L[0])
    while i<len(L)-2:
        if type(L[i])==type(L[i+1])!=type(L[i+2]):
            l=type(L[i+2])
        elif type(L[i])==type(L[i+2])!=type(L[i+1]):
            l=type(L[i+1])
        elif type(L[i+1])==type(L[i+2])!=type(L[i]):
            l=type(L[i])
        i+=1
    if l==int:
        return 'int'
    elif l==float:
        return 'float'
    elif l==str:
        return 'str'
    elif l==bool:
        return 'bool'
        
print(odd_one([2,1,2,3,6,7,8,9.5]))

        
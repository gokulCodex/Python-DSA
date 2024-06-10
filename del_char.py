def del_char(s,c):
    if len(c)>1:
        return s
    L=[]
    for i in s:
        if i!=c:
            L.append(i)
    str=L[0]
    for j in range(1,len(L)):
        str=str+L[j]
    return str

print(del_char('banana','a'))
def prime(num):                
    count=0
    for i in range(1,num+1):
        if num%i==0:
            count+=1
    if count==2:
        return True
    else:
        return False
def prime_product(m):
    if m<=0:
        return False
    set=[]
    for i in range(2,m):
        if prime(i):
            set.append(i)
    left=0
    right=len(set)-1
    while left<=right:
        prod=set[left]*set[right]
        if prod>m:
            right-=1
        elif prod<m:
            left+=1
        else:
            return True
    return False

print(prime_product(6))


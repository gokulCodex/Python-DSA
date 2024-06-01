def prime(num):                #Function to check primes less than n
    count=0
    for i in range(1,num+1):
        if num%i==0:
            count+=1
    if count==2:
        return True
    else:
        return False
def Goldbach(n):
    prime_set=[]
    for i in range(2,n):
        if prime(i):
            prime_set.append(i)
    left=0
    right=len(prime_set)-1
    op=[]
    while left<=right:
        sum=prime_set[left]+prime_set[right]
        if sum==n:
            op.append((prime_set[left],prime_set[right]))
            left+=1
            right-=1
        elif sum>n:
            right-=1
        elif sum<n:
            left+=1
    return op
print(Goldbach(34))
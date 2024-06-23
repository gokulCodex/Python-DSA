def merge(arr1,arr2):                   
    (m,n)=(len(arr1),len(arr2))
    C,i,j,k=[],0,0,0
    while k<m+n:
        if i==m:
            C.extend(arr2[j:])
            k+=n-j
        elif j==n:
            C.extend(arr1[:i])
            k+=n-i
        elif arr1[i]<arr2[j]:
            C.append(arr1[i])
            i+=1
            k+=1
        else:
            C.append(arr2[j])
            j+=1
            k+=1
    return C

def merge_sort(a):
    if len(a)<=1:
        return 
    mid=len(a)//2
    left_half=a[:mid]
    right_half=a[mid:]
    L=merge_sort(left_half)
    R=merge_sort(right_half)
    arr=merge(L,R)
    return arr

print(merge_sort([3,5,4,8,4,1,2]))
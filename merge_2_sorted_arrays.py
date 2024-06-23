def merge(arr1,arr2):                     #general merge function for merging 2 sorted arraays
    merged_arr=[]
    i,j=0,0
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<arr2[j]:
            merged_arr.append(arr1[i])
            i+=1
        elif arr1[i]>arr2[j]:
            merged_arr.append(arr2[j])
            j+=1
        else:
            merged_arr.append(arr1[i])
            merged_arr.append(arr2[j])
            i+=1
            j+=1
    while i<len(arr1):
        merged_arr.append(arr1[i])
        i+=1
    while j<len(arr2):
        merged_arr.append(arr2[j])
        j+=1
    return merged_arr
print(merge([2,3,5,8],[1,4,5,7]))




def fun(nums,target):
    left, right = 0, len(nums) - 1    
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1        
    return left
print('The target should be at the index: ',fun([1,2,4,5,6],3))
            

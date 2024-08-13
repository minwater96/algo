def arrayPairSum(nums):
    nums.sort()
    print(nums)    
    max_sum = sum(nums[::2])
    print(nums[::2])    
    return max_sum



print(arrayPairSum([1, 4, 3, 2])) # => 4
print(arrayPairSum([6,2,6,5,1,2])) # => 9
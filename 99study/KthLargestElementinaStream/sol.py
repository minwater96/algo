class KthLargest:
    num = []

    def __init__(self, k, nums):
        self.k = k
        self.nums = nums
        

    def add(self, val): #-> int:
        self.nums = self.nums + [val]
        self.nums = sorted(self.nums, reverse=True)
        print(self.nums)
        return self.nums[self.k-1] 

# input
# ["KthLargest", "add", "add", "add", "add", "add"]
# [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
# output
# [null, 4, 5, 5, 8, 8]

# https://leetcode.com/problems/kth-largest-element-in-a-stream/description/
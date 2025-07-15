Leetcode - 8

Array Partition

class Solution(object):
    def arrayPairSum(self, nums):
        nums.sort()  # Step 1: Sort the array
        result = 0
        for i in range(0, len(nums), 2):
            result += nums[i]  # Step 2: Add every alternate (even index) number
        return result

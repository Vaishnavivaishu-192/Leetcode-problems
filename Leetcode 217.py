Leetcode-42

217 Contains Duplicate


class Solution(object):
    def containsDuplicate(self, nums):
        nums.sort()
        n=len(nums)
        for i in range(1,n):
            if nums[i]==nums[i-1]:
                return True     
        return False
        
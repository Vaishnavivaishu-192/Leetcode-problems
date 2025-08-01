Leetcode-25

414.Third Maximum Number

class Solution(object):
    def thirdMax(self, nums):
        nums = list(set(nums))
        nums.sort()

        if (len(nums) < 3):
            return max(nums)
        else:
            return nums[-3]
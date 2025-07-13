Leetcode - 6 

Single number

class Solution(object):
    def singleNumber(self, nums):
        x=0
        for i in nums:
            x^=i
        return x
Leetcode - 7

Missing Number

class Solution(object):
    def missingNumber(self, nums):
      i=len(nums) 
      m=i*(i+1)//2
      n=sum(nums)
      return m-n
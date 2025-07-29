Leetcode-22
 
3289 The Two Sneaky Numbers of Digitville

class Solution(object):
    def getSneakyNumbers(self, nums):
        res=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j] and nums[i] not in res:
                    res.append(nums[i])
        return res
Leetcode 219

219 Contains Duplicate II

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        i=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if abs(i-j)<=k and nums[i]==nums[j]:
                    return True 
            
        return False
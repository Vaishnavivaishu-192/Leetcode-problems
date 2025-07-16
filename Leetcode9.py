Leetcode - 9
Intersection of two array

class Solution(object):
    def intersection(self, nums1, nums2):
        n = set(nums1)
        
        output = []
        for i in nums2:
            if i in n:
                output.append(i)
                n.remove(i)
            
        return output
Leetcode - 34

350 intersection of two arrays 

class Solution(object):
    def intersect(self, nums1, nums2):
        m=[]
        for num in nums1:
            if num in nums2:
                m.append(num)
                nums2.remove(num)
        return m
        
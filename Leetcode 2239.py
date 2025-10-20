Leetcode - 97

2239 Find Closest Number to Zero


class Solution(object):
    def findClosestNumber(self, nums):
        clst=nums[0]
        for x in nums:
            if abs(x) < abs(clst):
                clst = x
        if clst < 0 and abs(clst) in nums:
            return abs(clst)
        else:
            return clst
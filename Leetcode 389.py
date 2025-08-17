Leetcode - 41

389 Find the Difference

class Solution(object):
    def findTheDifference(self, s, t):
        for i in t:
            if s.count(i)!=t.count(i):
                return i 


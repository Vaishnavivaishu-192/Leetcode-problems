Leetcode-47

205. Isomorphic String

class Solution(object):
    def isIsomorphic(self, s, t):
        new1 = []
        new2 = []
        for idx in s:
            new1.append(s.index(idx))
        for idx in t:
            new2.append(t.index(idx))
        if new1 == new2:
            return True
        return False  
        
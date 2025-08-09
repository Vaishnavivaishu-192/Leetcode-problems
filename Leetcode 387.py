Leetcode - 33

387 First unique Character in a String

class Solution(object):
    def firstUniqChar(self, s):
        mset = collections.Counter(s)
        for idx in range(len(s)):
            if mset[s[idx]] == 1:
                return idx
        return -1 
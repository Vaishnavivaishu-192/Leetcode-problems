Leetcode - 91

3541 Find Most Frequent Vowel and Consonant

class Solution(object):
    def maxFreqSum(self, s):
        con = 0
        vow = 0
        resset = set(s)
        for i in resset:
            if i in "aeiou":
                vow = max(vow, s.count(i))
            else:
                con = max(con, s.count(i))
        return con+vow  
Leetcode - 55

392 Is Subsequence

class Solution:
    def isSubsequence(self, s, t):
        if not s:
            return True 
        correct = len(s)
        start = 0
        for letter in t:
            if s[start] == letter:
                start += 1
            if start == correct:
                return True
        return False
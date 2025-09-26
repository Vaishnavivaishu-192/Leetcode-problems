Leetcode - 77

1332 Remove Palindromic Subsequences

class Solution(object):
    def removePalindromeSub(self, s):
        if s == s[::-1]:
            return 1
        else:
            return 2
        
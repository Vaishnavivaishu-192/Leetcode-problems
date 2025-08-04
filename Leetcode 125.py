Leetcode - 28

125.Valid Palindrome

class Solution(object):
    def isPalindrome(self, s):
        s = s.lower()
        original = ""
        reverse = ""

        for char in s:
            if char.isalnum():
                original += char
                reverse = char + reverse

        return original == reverse
        
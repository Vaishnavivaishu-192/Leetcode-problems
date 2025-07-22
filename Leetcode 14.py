Leetcode - 15

14. Longest Common Prefix

class Solution:
    def longestCommonPrefix(self, strs):
        first_str = min(strs, key=len)
        for i in range(len(first_str)):
            for _str in strs:
                if _str[i] != first_str[i]:
                    return first_str[:i]
        return first_str
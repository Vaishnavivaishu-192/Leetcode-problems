Leetcode - 66

1576 Replace All ? to a avoid consecutive repeating characters 

class Solution(object):
    def modifyString(self, s):
        s = list(s)  
        for i in range(len(s)):
            if s[i] == '?':
                for ch in "abc":
                    if (i > 0 and s[i-1] == ch) or (i < len(s)-1 and s[i+1] == ch):
                        continue
                    s[i] = ch
                    break
        return "".join(s)

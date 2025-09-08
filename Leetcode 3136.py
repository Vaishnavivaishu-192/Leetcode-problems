Leetcode - 62

3136 Valid Word


class Solution:
    def isValid(self, s):
        if len(s)<3:
            return False
        vow=0
        con=0
        vowels="aeiouAEIOU"
        for c in s:
            if c.isalpha():
                if c in vowels:
                    vow += 1
                else:
                    con += 1
            elif not c.isdigit():
                return False  
        return vow >= 1 and con >= 1
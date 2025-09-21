Leetcode - 73

1221 Split a String in Balancd Strings

class Solution:
    def balancedStringSplit(self, S):
        m = c = 0
        for s in S:
            if s == 'L': 
                c += 1
            if s == 'R': 
                c -= 1
            if c == 0: 
                m += 1
        return m
Leetcode - 65

2315 Count Asterisks

class Solution(object):
    def countAsterisks(self, s):
        ans = 0
        flag = True
        for ch in s:
            if flag and ch == '*':
                ans += 1
            if ch == '|':
                flag = not flag
        return ans
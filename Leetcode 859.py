Leetcode - 79

859 Buddy Strings


class Solution(object):
    def buddyStrings(self, s, goal):
        if len(s) != len(goal):
            return False
        if s == goal:
            return len(set(s)) < len(s)
        diffs = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                diffs.append(i)
        if len(diffs) != 2:
            return False
        i, j = diffs
        return s[i] == goal[j] and s[j] == goal[i]
       
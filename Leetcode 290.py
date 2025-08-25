Leetcode-48

290. Word Pattern

class Solution(object):
    def wordPattern(self, pattern, s):
        words = s.split()
        if len(pattern) != len(words):
            return False
        new1 = []
        new2 = []
        for ch in pattern:
            new1.append(pattern.index(ch))
        for w in words:
            new2.append(words.index(w))

        return new1 == new2

Leetcode- 21

Counting words With a Given Prefix

class Solution(object):
    def prefixCount(self, words, pref):
        count = 0
        for word in words:
            if word[:len(pref)] == pref:
                count += 1
        return count


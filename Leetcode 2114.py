Leetcode- 20

2114 Maximum Number of Words Found in Sentences

class Solution(object):
    def mostWordsFound(self, sentences):
        m = 0
        for i in sentences:
            result = list(map(str, i.split()))
            m = max(m, len(result))
        return m

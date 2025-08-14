Leetcode - 38

884 Uncommon Words from two sentences

class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        count = Counter((s1 + ' ' + s2).split(' '))
        res = []
        for i in count.keys():
            if count[i] < 2:
                res.append(i)

        return res
Leetcode - 58

557 Reverse Words in a String III

class Solution(object):
    def reverseWords(self, s):
        n=s.split()
        m=[]
        for i in n:
            m.append(i[::-1])
        return ' '.join(m)

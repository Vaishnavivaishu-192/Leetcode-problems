Leetcode - 100

1941 check if all characters have equal number of occurrences


class Solution:
    def areOccurrencesEqual(self, s):
        d={}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        t=d[s[0]]
        for v in d.values():
            if v!=t:
                return False
        return True
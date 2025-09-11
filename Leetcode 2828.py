Leetcode - 64

2828 Check if a String is an Acronym of Words

class Solution(object):
    def isAcronym(self, words, s):
        if len(words)!=len(s):
            return False
        for i in range(len(s)):
            if len(words[i])==0 or words[i][0]!=s[i]:
                return False
        return True
        
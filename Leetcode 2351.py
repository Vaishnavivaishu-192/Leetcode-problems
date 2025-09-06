Leetcode - 60 

2351 First Letter to Appear Twice

class Solution(object):
    def repeatedCharacter(self, s):
        sets=set()
        for word in s:
            if word in sets:
                return word
            else:
                sets.add(word)
             

        
Leetcode - 68

796 Rotate String 

class Solution(object):
    def rotateString(self,s,goal):
        if len(s)!=len(goal):
            return False
        for i in range(len(goal)):
            if goal[i]==s[0]:
                t=goal[i:]+goal[:i]
                if t==s:
                    return True
        return False
        
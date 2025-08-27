Leetcode-50

1047 Remove All Adjacent Duplicates in String

class Solution(object):
    def removeDuplicates(self, s):
        new1=[]
        for ch in s:
            if new1 and new1[-1] ==ch:
                new1.pop()
            else:
                new1.append(ch)    
        return "".join(new1)
Leetcode - 63

1189 Maximum Number of Balloons

class Solution(object):
    def maxNumberOfBalloons(self, text):
        dic={'b':0,'a':0,'l':0,'o':0,'n':0}
        for char in text:
            if char in dic:
                dic[char]+=1
        dic['l']//=2
        dic['o']//=2
        return min(dic.values())
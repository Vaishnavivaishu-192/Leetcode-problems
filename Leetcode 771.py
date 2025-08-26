Leetcode - 49

771 Jewels and Stones

class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        jewelnew1=set(jewels)
        count=0
        for stone in stones:
            if stone in jewelnew1:
                count+=1
        return count 
        
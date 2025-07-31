Leetcode-24

1431 Kids With the Greatest number of Candies

class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        i=0
        result=[]
        n=max(candies)
        for i in range(len(candies)):
            if candies[i]+extraCandies>=n:
                result.append(True)
            else:
                result.append(False)
        return result
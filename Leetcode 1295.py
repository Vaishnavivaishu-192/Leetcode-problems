Leetcode - 70

1295 Find Numbers with Even Number of Digits

class Solution(object):
    def findNumbers(self, nums):
        count=0
        for i in nums:
            if len(str(i))%2==0:
                count+=1
            else:
                continue
        return count
Leetcode - 71

1748 Sum of Unique Elements

class Solution(object):
    def sumOfUnique(self, nums):
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        total = 0
        for num, freq in count.items():
            if freq == 1:
                total += num
        return total


        
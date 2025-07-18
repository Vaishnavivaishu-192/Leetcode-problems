Leetcode 3190

Find Minimum Operations to Make All Elements Divisible by Three

class Solution:
    def minimumOperations(self, nums):
        count = 0
        for num in nums:
            if num % 3 == 1 or num % 3 == 2:
                count += 1
        return count
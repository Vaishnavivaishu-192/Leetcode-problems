Leetcode - 96

3432 Count Partitions with Even Sum Difference


class Solution(object):
    def countPartitions(self, nums):
        n = len(nums)
        totalSum = sum(nums)
        leftSum = 0
        count = 0
        for i in range(n - 1):
            leftSum += nums[i]
            rightSum = totalSum - leftSum
            if (leftSum - rightSum) % 2 == 0:
                count += 1

        return count
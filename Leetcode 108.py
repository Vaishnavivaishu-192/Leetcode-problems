Leetcode-45

108 Convert Sorted Array to Binary Search Tree

class Solution(object):
    def sortedArrayToBST(self, nums):
        def rec(nums, start, end):
            if start <= end:
                mid = (start + end) // 2
                node = TreeNode(nums[mid])
                node.left = rec(nums, start, mid - 1)
                node.right = rec(nums, mid + 1, end)
                return node
        return rec(nums, 0, len(nums) - 1)
        
            
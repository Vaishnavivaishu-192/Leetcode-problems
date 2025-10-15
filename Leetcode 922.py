Leetcode - 94

922 Sort Array by parity II

class Solution(object):
    def sortArrayByParityII(self, nums):
        i,j=0,1
        n=len(nums)
        while i<n and j<n:
            if nums[i]%2==0:
                i+=2
            elif nums[j]%2==1:
                j+=2
            else:
                nums[j],nums[i]=nums[i],nums[j]
                i+=2
                j+=2
        return nums
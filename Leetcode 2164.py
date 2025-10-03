Leetcode - 84

2164 Sort Even and Odd Indices Independently

class Solution(object):
    def sortEvenOdd(self, nums):
        even_nums = sorted(nums[::2])             
        odd_nums = sorted(nums[1::2], reverse=True)  
        result = []
        e = o = 0
        for i in range(len(nums)):
            if i % 2 == 0:  
                result.append(even_nums[e])
                e += 1
            else:            
                result.append(odd_nums[o])
                o += 1
        return result
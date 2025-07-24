Leetcode - 17

905 Sort Array by parity

class Solution(object):
    def sortArrayByParity(self, nums):
        odd_number=[]
        even_number=[]
        for num in nums:
            if num%2==0:
                even_number.append(num)
            else:
                odd_number.append(num)
        result=even_number+odd_number        
        return result
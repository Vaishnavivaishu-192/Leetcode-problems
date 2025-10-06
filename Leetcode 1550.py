Leetcode - 87

1550 Three Consecutive Odds


class Solution(object):
    def threeConsecutiveOdds(self, arr):
        count = 0
        for i in range(len(arr)):
            if arr[i] % 2 != 0: 
                count += 1
                if count == 3:
                    return True
            else:
                count = 0
        return False

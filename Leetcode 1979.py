Leetcode - 72

1979 Find Greatest Common Divisor of Array


class Solution(object):
    def findGCD(self, nums):
        mn = min(nums)
        mx = max(nums)
        divs = []

        for i in range(1, mn+1):
            if mx % i == 0 and mn % i == 0:
                divs.append(i)

        gcd = max(divs)

        return gcd
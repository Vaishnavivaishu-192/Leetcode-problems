Leetcode - 89

2923 Find Champion I

class Solution:
    def findChampion(self, grid):
        n = len(grid)
        for i in range(n):
            if sum(grid[i]) == n - 1:
                return i
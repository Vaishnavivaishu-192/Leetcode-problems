Leetcode 52

1528 Shuffle String 

class Solution(object):
    def restoreString(self, s, indices):
        ans = "" 
        for i in range(len(indices)): 
            ans += s[indices.index(i)]  
        return ans 
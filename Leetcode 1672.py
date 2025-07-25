Leetcode-18

1672 Richest Customer Wealth

class Solution(object):
    def maximumWealth(self, accounts):
        maxi=0
        temp=[]
        for i in range(len(accounts)):
            total=sum(accounts[i])
            temp.append(total)
            largest=max(temp)
        return largest
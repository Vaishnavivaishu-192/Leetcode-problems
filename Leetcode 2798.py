Leetcode - 19 

2798 Number of Employees Who met the Target

class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        count=0
        for i in range(len(hours)):
            if hours[i]>=target:
                count+=1
        return count
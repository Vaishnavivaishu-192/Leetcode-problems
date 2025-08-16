Leetcode - 40

551 Student Attendance Record I

class Solution(object):
    def checkRecord(self, s):
        for char in set(s):
            if s.count("A")>=2:
                return False
            elif "LLL" in s:
                return False
            else:
                return True
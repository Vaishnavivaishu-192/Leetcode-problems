Leetcode - 81

657 Robot Return to Origin

class Solution(object):
    def judgeCircle(self, moves):
        lr=0
        ud=0
        for move in moves:
            if move=='U':
                ud+=1
            elif move=='D':
                ud-=1
            elif move=='L':
                lr+=1
            elif move=='R':
                lr-=1
        if lr==0 and ud==0:
            return True
        else:
            return False


        
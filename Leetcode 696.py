Leetcode- 46

696 Count Binary Substrings

class Solution:
    def countBinarySubstrings(self,  str):
        pre= 0
        count= 1
        actual= 0
        for i in range(1,len(str)):
            if(str[i]==str[i-1]):
                count+=1
            else:
                actual+= min(pre,count)
                pre= count
                count= 1

        actual+= min(pre,count)

        return actual
Leetcode-29

344 Reverse string 

class solution(object):
def reverseString(self,s):
start=0
last=len(s)-1
while start<=last:
temp=s[start]
s[start]=s[last]
s[last]=temp
start+=1
last-=1
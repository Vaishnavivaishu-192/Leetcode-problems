class Solution(object) :

def strstr(self, haystack, needle):

For i in range(len(haystack)):

if haystack[i:i+len(needle)]== needle:

return 0

else:

return -1
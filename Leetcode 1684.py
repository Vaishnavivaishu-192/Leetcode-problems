Leetcode - 59

1684 Count the Number of consistent Strings

class Solution:
    def countConsistentStrings(self, allowed, words):
        allowed = set(allowed)
        count = 0
        for word in words:
            for letter in word:
                if letter not in allowed:
                    count += 1
                    break
        
        return len(words) - count
                
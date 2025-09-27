Leetcode - 78 

1408 String Matching in an array 


class Solution:
    def stringMatching(self, words):
        result = []
        n = len(words)
        for i in range(n):
            for j in range(n):
                if i != j and words[i] in words[j]:
                    result.append(words[i])
                    break
        return result
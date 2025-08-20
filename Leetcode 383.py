Leetcode - 44

383 Ransom Note


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        ransom_counter = Counter(ransomNote)
        magazine_counter = Counter(magazine)

        for char in ransom_counter:
            if ransom_counter[char] > magazine_counter.get(char, 0):
                return False
        return True
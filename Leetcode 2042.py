Leetcode - 80

2024 Check if Numbers are ascending in a Sentence

class Solution(object):
    def areNumbersAscending(self, s):
	previous = -1
	for w in s.split():
		if w.isdigit():
			if int(w) <= previous:
				return False
			previous = int(w)

	return True
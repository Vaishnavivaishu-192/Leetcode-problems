Leetcode - 53

599 Minimum Index Sum of Two Lists

class Solution(object):
    def findRestaurant(self, list1, list2):
        common = []
        min_sum = len(list1) + len(list2)   
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    if i + j < min_sum:
                        min_sum = i + j
                        common = [list1[i]]
                    elif i + j == min_sum:
                        common.append(list1[i])

        return common
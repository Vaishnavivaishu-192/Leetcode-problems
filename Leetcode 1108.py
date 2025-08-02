Leetcode-26

1108 Defanging an IP Address


class Solution(object):
    def defangIPaddr(self, address):
        add = list(address) 
        output = []  
        for i in add:
            if i == ".":
                output.extend(["[", ".", "]"])  
            else:
                output.append(i) 

        return ''.join(output) 
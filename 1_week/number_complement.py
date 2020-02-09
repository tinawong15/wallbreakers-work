class Solution:
    def findComplement(self, num: int) -> int:
        binary_rep = "{0:b}".format(num)
        complement = ''
        for char in binary_rep:
            if char == '0':
                complement += "1"
            else:
                complement += "0"
        return int(complement, 2)

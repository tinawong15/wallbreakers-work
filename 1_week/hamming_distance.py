class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x_binary = "{0:b}".format(x)
        y_binary = "{0:b}".format(y)
        if len(x_binary) > len(y_binary):
            max_size = len(x_binary)
        else:
            max_size = len(y_binary)
        for i in range(max_size-len(x_binary)):
            x_binary = "0"+x_binary
        for i in range(max_size-len(y_binary)):
            y_binary = "0"+y_binary
        diff = 0
        for i in range(len(x_binary)):
            if x_binary[i] != y_binary[i]:
                diff += 1
        return diff

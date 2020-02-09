class Solution:
    def binaryGap(self, N: int) -> int:
        binary_rep = "{0:b}".format(N)
        max_gap = 0
        last_index = 0
        for i in range(len(binary_rep)):
            if binary_rep[i] == "1":
                gap = i - last_index
                if gap > max_gap:
                    max_gap = gap
                last_index = i
        return max_gap

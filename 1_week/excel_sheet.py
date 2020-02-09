class Solution:
    def titleToNumber(self, s: str) -> int:
        col_num = 0
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        digit = 0
        for i in range(len(s)):
            col_num += (alphabet.find(s[-(i+1)])+1) * (26**digit)
            print(s[-(i+1)])
            print(alphabet.find(s[-(i+1)]))
            digit += 1
        return col_num

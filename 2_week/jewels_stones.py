class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewels = 0
        for char in J:
            jewels += S.count(char)
        return jewels

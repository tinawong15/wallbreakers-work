class Solution:
    def firstUniqChar(self, s: str) -> int:
        already_passed = []
        for i in range(len(s)):
            if s[i] not in s[i+1:] and s[i] not in already_passed:
                return i
            already_passed.append(s[i])
        return -1
            

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        letters = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] not in letters.keys():
                if t[i] in letters.values():
                    return False
                letters[s[i]] = t[i]
            else:
                if t[i] != letters[s[i]]:
                    return False

        return True

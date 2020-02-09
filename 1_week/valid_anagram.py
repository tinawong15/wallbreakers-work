class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_freq = {char:s.count(char) for char in s}
        t_freq = {char:t.count(char) for char in t}

        if s_freq.items() != t_freq.items():
            return False
        return True

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        if strs != []:
            in_word = True
            min_word = strs[0]
            for word in strs[1:]:
                if len(word) < len(min_word):
                    min_word = word
            for i in range(len(min_word)):
                for word in strs:
                    if min_word[i] != word[i]:
                        in_word = False
                if in_word:
                    prefix += min_word[i]
        return prefix

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) == 1:
            return True
        elif word[0] == word[0].lower() or (word[0] == word[0].upper() and word[1] == word[1].lower()):
            for character in word[1:]:
                if character != character.lower():
                    return False
        else:
            for character in word[1:]:
                if character != character.upper():
                    return False
        return True

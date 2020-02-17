class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        str_list = str.split(" ")
        word_dict = {}
        if len(str_list) != len(pattern):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in word_dict and str_list[i] not in word_dict.values():
                word_dict[pattern[i]] = str_list[i]
            else:
                if pattern[i] not in word_dict and str_list[i] in word_dict.values():
                    return False
                excluding_current_word = [value for key, value in word_dict.items() if key != pattern[i]]
                if str_list[i] != word_dict[pattern[i]] or str_list[i] in excluding_current_word:
                    return False
        return True
        

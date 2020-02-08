class Solution:
    def reverseWords(self, s: str) -> str:
        str_list = s.split(" ")
        char_list = []
        for word in str_list:
            char_list.append([char for char in word])
        for word in char_list:
            for i in range(len(word)//2):
                temp = word[i]
                word[i] = word[-(i+1)]
                word[-(i+1)] = temp
        # print(char_list)
        result = ''
        for word in char_list:
            for char in word:
                result += char
            result += " "
        result = result.strip()
        return result

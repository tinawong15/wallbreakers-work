class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ["a","e","i","o","u","A","E","I","O","U"]
        split_word = [char for char in s]
        vowels_index = []
        vowels_in_word = []
        for i in range(len(s)):
            if s[i] in vowels:
                vowels_index.append(i)
                vowels_in_word.append(s[i])

        for i in range(len(vowels_in_word) // 2):
            temp = vowels_in_word[i]
            vowels_in_word[i] = vowels_in_word[-(i+1)]
            vowels_in_word[-(i+1)] = temp

        index_vowels_in_word = 0

        for i in range(len(split_word)):
            if index_vowels_in_word < len(vowels_index) and i == vowels_index[index_vowels_in_word]:
                split_word[i] = vowels_in_word[index_vowels_in_word]
                index_vowels_in_word += 1

        result = "".join([char for char in split_word])
        return result
            

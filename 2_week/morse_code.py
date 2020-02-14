class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        results = set()
        for word in words:
            result = ""
            for char in word:
                result += morse[alphabet.index(char)]
            results.add(result)
        count = len(results)
        return count

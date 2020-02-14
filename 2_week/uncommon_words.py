class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        words = {}
        for word in A.split(" "):
            if word in words.keys():
                words[word] += 1
            else:
                words[word] = 1
        for word in B.split(" "):
            if word in words.keys():
                words[word] += 1
            else:
                words[word] = 1
        uncommon = [key for key, value in words.items() if value == 1]
        return uncommon

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        paragraph = re.split(r"\s+|[!?',;.-]\s*", paragraph)
        freq = {}
        for word in paragraph:
            if word not in banned and word != '':
                if word not in freq:
                    freq[word] = 1
                else:
                    freq[word] += 1
        print(freq)
        values = list(freq.values())
        key = list(freq.keys())
        return key[values.index(max(values))]

class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        sister = set()
        for i in range(len(candies)):
            sister.add(candies[i])
        return min(len(sister), len(candies) // 2)
        

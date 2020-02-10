class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num_count = {}
        for num in nums:
            if num not in num_count:
                num_count[num] = 1
            else:
                num_count.pop(num)
        return num_count.popitem()[0]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {value: index for index, value in enumerate(nums)}

        for index, value in enumerate(nums):
            if target - value in indices and index != indices[target-value]:
                return [indices[target-value], index]
            

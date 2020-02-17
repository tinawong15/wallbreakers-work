class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        with_duplicates = [num for num in nums1 if num in nums2]
        with_duplicates_set = set(with_duplicates)
        return list(with_duplicates_set)
        

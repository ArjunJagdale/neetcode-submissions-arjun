class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        h = {num:i for i, num in enumerate(nums2)}
        res = []
        
        for i in nums1:
            res.append(h[i])
        
        return res
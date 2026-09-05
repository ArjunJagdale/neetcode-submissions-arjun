class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hm = {}

        for i, num in enumerate(nums):
            if num in hm and i - hm[num] <= k:
                return True
            
            hm[num] = i
        
        return False

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        h = {}

        for i in nums:
            h[i] = h.get(i, 0) + 1
        
        for i in h:
            if h[i] >= len(nums) // 2:
                return i
        
        return -1
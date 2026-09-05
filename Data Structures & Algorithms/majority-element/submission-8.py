class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hm = {}
        res = 0

        limit = len(nums) // 2
        for i in nums:
            hm[i] = hm.get(i, 0) + 1
            if hm[i] > limit:
                res = i
        
        return res
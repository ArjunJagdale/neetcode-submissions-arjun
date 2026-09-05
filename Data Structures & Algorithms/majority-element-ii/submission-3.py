class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        h = {}
        n = len(nums)
        limit = n // 3
        res = []

        for i in nums:
            h[i] = h.get(i, 0 ) + 1
        
        for i in h:
            if h[i] > limit:
                res.append(i)
        
        return res

        
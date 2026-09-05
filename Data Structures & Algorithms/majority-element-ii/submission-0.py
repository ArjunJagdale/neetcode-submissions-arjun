class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        n = len(nums)
        h = {}
        res = []
        for i in nums:
            h[i] = h.get(i, 0) + 1
    
        for i in h:
            if h[i] > n/3:
                res.append(i)
        
        return res
        
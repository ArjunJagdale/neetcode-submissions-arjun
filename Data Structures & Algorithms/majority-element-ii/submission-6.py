class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hm = {}
        limit = len(nums) // 3
        res = set()
        for num in nums:
            hm[num] = hm.get(num, 0) + 1
            if hm[num] > limit:
                res.add(num)
        
        return list(res)

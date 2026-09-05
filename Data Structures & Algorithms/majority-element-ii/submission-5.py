class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)
        limit = n // 3
        hashmap = {}

        for i in nums:
            hashmap[i] = hashmap.get(i, 0) + 1
            if hashmap[i] > limit and i not in res:
                res.append(i)
        
        return res



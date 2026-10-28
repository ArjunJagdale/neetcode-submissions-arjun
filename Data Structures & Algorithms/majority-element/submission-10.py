class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}
        limit = len(nums) // 2

        for i in nums:
            hashmap[i] = hashmap.get(i, 0) + 1
            if hashmap[i] > limit:
                return i

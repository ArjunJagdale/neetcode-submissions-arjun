class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash_map = {}

        for i in nums:
            hash_map[i] = hash_map.get(i, 0) + 1
        
        max_key = max(hash_map, key = hash_map.get)

        return max_key
        
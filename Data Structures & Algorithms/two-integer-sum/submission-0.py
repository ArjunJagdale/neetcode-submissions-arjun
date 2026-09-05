class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        h_map = {}

        for i, j in enumerate(nums):
            complement = target - j

            if complement in h_map:
                return [h_map[complement], i]

            h_map[j] = i
            

        
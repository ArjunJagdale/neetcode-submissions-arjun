class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        nums = [0] + nums
        rs = sum(nums)
        ls = 0

        for i in range(1, len(nums)):
            rs = rs - nums[i]
            ls = ls + nums[i-1]

            if ls == rs:
                return i - 1
        
        return -1
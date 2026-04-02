class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()

        i, j = 0, k - 1
        min_diff = 100000

        while j < len(nums):
            diff = nums[j] - nums[i]
            min_diff = min(min_diff, diff)
            i, j = i+1, j+1
        
        return min_diff

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        # 1,2,3,3,5,6
        # k = 3
        min_d = 100001
        i = 0
        j = i + k - 1

        while j < len(nums):
            diff = nums[j] - nums[i] # 2, 1, 2, 3
            min_d = min(diff, min_d) # 2, 1, 1, 1
            i += 1
            j += 1
        
        return min_d
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = 0
        for i in nums:
            total += i

        lp = 0

        for i in range(len(nums)):
            rp = total - nums[i] - lp

            if lp == rp:
                return i
            
            lp += nums[i]
        
        return -1
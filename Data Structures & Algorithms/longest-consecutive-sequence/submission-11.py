class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums= set(nums)
        longest = 0
        for i in range(len(nums)):
            if nums[i] - 1 not in set_nums:
                index = 0
                while nums[i] + index in set_nums:
                    index += 1
                longest = max(longest, index)
        
        return longest
                
                

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0

        if len(nums) <= 1:
            return 1

        for i in range(len(nums)):
            if nums[i] != nums[i-1]:
                nums[k] = nums[i]
                k += 1
        
        return k
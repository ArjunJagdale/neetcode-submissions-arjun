class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 0

        if len(nums) <= 1:
            return 1
        
        for i in range(len(nums)):
            if nums[i] != nums[i-1]:
                nums[index] = nums[i]
                index += 1
        return index

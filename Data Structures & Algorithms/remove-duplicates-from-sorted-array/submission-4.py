class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 1

        for num in range(1, len(nums)):
            if nums[num-1] != nums[num]:
                nums[index] = nums[num]
                index += 1
        
        return index

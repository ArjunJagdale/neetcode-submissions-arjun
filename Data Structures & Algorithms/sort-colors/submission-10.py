class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # use count sort
        # as we know there are numbers from range 0 to 2, we can have their count
        count = [0] * 3
        for i in nums:
            count[i] += 1
        
        index = 0

        for i in range(3):
            while count[i]:
                count[i] -= 1
                nums[index] = i
                index += 1

        
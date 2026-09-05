class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # as we have only 3 color, let us have an array of len 3
        count = [0] * 3

        # now let us increment the occurance count of each ele in input array
        for i in nums:
            count[i] += 1
        
        # let us have an index to be updated
        index = 0

        for i in range(3):
            while count[i]:
                count[i] -= 1
                nums[index] = i
                index += 1
        
        return nums
        
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # nums = [1,1,2,3,4], val = 1
# nums = [4,1,2,3]
# nums = [4,3,2]
        
        i = 0
        n = len(nums)

        while i < n:
            if nums[i] == val:
                n -= 1
                nums[i] = nums[n]
            else:
                i += 1
        
        return n

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        last = len(res)-1

        i = 0
        j = len(nums) - 1

        while i <= j:
            if nums[i]*nums[i] > nums[j]*nums[j]:
                res[last] = nums[i]*nums[i]
                last -= 1
                i += 1
            else:
                res[last] = nums[j]*nums[j]
                last -= 1
                j -= 1
        
        return res
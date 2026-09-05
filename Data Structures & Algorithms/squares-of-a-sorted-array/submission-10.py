class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i, j = 0, len(nums) - 1
        res = [0] * len(nums)
        last = len(res) - 1

        while i <= j:
            if nums[i] * nums[i] > nums[j] * nums[j]:
                res[last] = nums[i]*nums[i]
                i += 1
                last -= 1
            else:
                res[last] = nums[j]*nums[j]
                j -= 1
                last -= 1
        
        return res
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return [nums[0] ** 2]
        
        i = 0
        resi = j = len(nums) - 1
        res = [0] * len(nums)
        
        while i < j:
            if abs(nums[i]) < abs(nums[j]):
                res[resi] = nums[j] ** 2
                resi -= 1
                j -= 1

            else:
                res[resi] = nums[i] ** 2
                resi -= 1
                i += 1
            
            res[resi] = nums[i] ** 2

        return res
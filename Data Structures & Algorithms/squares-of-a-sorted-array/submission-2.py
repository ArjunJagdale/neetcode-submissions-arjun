class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i = 0 
        j = len(nums) - 1
        res = [0] * len(nums)
        resp = len(res) - 1

        if len(nums) <= 1:
            return [nums[0] ** 2]

        while i < j:
            if abs(nums[i]) < abs(nums[j]):
                res[resp] = nums[j] ** 2
                resp -= 1
                j -= 1
            else:
                res[resp] = nums[i] ** 2
                resp -= 1
                i += 1
            res[resp] = nums[i] ** 2
        return res
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i = 0
        j = len(nums) - 1
        res = [0] * len(nums)

        for x in range(len(nums)):
            if nums[x] % 2 == 0:
                res[i] = nums[x]
                i += 1
            else:
                res[j] = nums[x]
                j -= 1
        return res
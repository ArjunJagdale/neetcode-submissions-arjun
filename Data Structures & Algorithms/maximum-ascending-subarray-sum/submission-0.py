class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        # iterate from to range
        # now check if nums[i] < nums[i-1]
        # if so then add them and store in s variable
        # also maintain res with max(res, s)
        # if desceding flow found, then s = 0
        res = add = prev = 0

        for i in range(len(nums)):
            if nums[i] > prev:
                add = add + nums[i] # 50 + 10 = 65
                res = max(res, add) # 65
            else:
                add = nums[i]
            prev = nums[i] # 50
        return res
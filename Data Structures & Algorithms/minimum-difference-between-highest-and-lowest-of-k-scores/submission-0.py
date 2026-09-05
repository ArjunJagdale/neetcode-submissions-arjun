class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        def quicksort(nums):
            if len(nums) <= 1:
                return nums
            pivot = nums[len(nums) // 2]
            left = [x for x in nums if x < pivot]
            mid = [x for x in nums if x == pivot]
            right = [x for x in nums if x > pivot]

            return quicksort(left) + mid + quicksort(right)
        
        nums = quicksort(nums)

        l, r = 0, k - 1
        res = float("inf")

        while r < len(nums):
            res = min(res, nums[r] - nums[l])
            l += 1
            r += 1
        
        return res
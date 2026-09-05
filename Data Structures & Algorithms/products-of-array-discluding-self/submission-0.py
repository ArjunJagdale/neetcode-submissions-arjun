class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = 1
        count = 0
    
        for i in nums:
            if i != 0:
                ans *= i
            else:
                count += 1
    
        res = [0] * len(nums)
        for i in range(len(nums)):
            if count >= 2:
                break
            elif nums[i] == 0:
                res = [0] * len(nums)
                res[i] = ans
                break
        
            res[i] = ans//nums[i]
        
        return res 
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_c = 0
        count = 0
        for i in nums:
            if i == 1:
                count += 1
                if count > max_c:
                    max_c = count
            else:
                count = 0
        
        return max_c

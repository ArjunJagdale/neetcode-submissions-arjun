class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # find first in seq
        # keep adding i with increasing value to check if it is there
        # if not, append to result array
        n = len(nums)
        nums_s = set(nums)
        s = set(range(1, n+1))

        res = []
        for i in s:
            if i not in nums_s:
                res.append(i)

        return res
        
        

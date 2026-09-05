class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums_s = set(nums)
        res_s = set(range(1, n+1))
        res = []

        for i in res_s:
            if i not in nums_s:
                res.append(i)
        
        return res
        
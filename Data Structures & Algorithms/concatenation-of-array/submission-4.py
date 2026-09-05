class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        res = []
        res[:] = nums[:]
        return res * 2
        
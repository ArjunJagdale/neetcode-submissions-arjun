class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        resDict = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in resDict:
                return [resDict[diff], i]
            resDict[n] = i
            
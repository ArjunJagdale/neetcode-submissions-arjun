class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        approch is to add [subset + [num] for subset in res] to "res"

        eg.
        res = [[]]
        subset = []
        num = 1

        result - res = [[], [1]]
        similary for other iterations

        result - res = [[], [1], [2], [1,2]]
        result - res = [[], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3]]
        """

        res = [[]]

        for num in nums:
            res += [subset + [num] for subset in res]

        return res
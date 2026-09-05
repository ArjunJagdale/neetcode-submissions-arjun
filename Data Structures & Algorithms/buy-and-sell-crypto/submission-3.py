class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # solution using DP
        min_p = float('inf')
        max_p = 0

        for p in prices:
            min_p = min(min_p, p)
            profit = p - min_p
            max_p = max(max_p, profit)
        
        return max_p
        
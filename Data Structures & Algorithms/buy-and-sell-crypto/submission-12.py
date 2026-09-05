class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = j = mp = 0 

        while i < len(prices) and j < len(prices):
            if prices[i] < prices[j]:
                p = prices[j] - prices[i]
                mp = max(mp, p) # 5
            else:
                i = j
            j += 1

        
        return mp

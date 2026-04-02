class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = 1
        mp = 0
        while i < len(prices) and j < len(prices):
            if prices[j] > prices[i]:
                p = prices[j] - prices[i]
                mp = max(mp, p)
            else:
                i = j
            j += 1  
        
        return mp
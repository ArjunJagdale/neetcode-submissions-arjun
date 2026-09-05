class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = 0
        p = 0
        mp = 0

        while i < len(prices) and j < len(prices):
            if prices[i] < prices[j]:
                p += prices[j] - prices[i]
                mp = max(mp, p)

            i = j  
            j += 1
        
        return mp
            
            
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = 0
        maxp = 0
        p = 0

        n = len(prices)

        while i < n and j < n:
            if prices[i] < prices[j]:
                p = prices[j] - prices[i]
                maxp += p
                i += 1
                
            elif prices[i] >= prices[j]:
                i = j
            
            j += 1
        
        return maxp
        